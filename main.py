import boto3
from botocore.config import Config
import json
from datetime import datetime

def blog_generation_using_bedrock(blogtopic: str) -> str:
    body = {
        "prompt": f"Write a blog of 200 words on the topic: {blogtopic}",
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        # Initialize Bedrock client
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                               config=Config(read_timeout=300, retries={'max_attempts': 3}))

        # Call Meta LLaMA 3 70B Instruct model
        response = bedrock.invoke_model(
            modelId="meta.llama3-70b-instruct-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        # Read and parse the response
        response_content = response['body'].read()
        response_data = json.loads(response_content)
        print("Bedrock Response:", response_data)

        blog_content = response_data.get('generation', 'No content returned')
        return blog_content

    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""

def save_blog_details_in_s3(s3_key, s3_bucket, blog_content):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=blog_content)
        print("Blog saved to S3")
    except Exception as e:
        print(f"Error saving the blog to S3: {e}")

def lambda_handler(event, context):
    try:
        event = json.loads(event['body'])
        blog_topic = event['blog_topic']
        print(f"Received blog topic: {blog_topic}")

        blog_content = blog_generation_using_bedrock(blog_topic)

        if blog_content:
            current_time = datetime.now().strftime('%Y%m%d%H%M%S')
            s3_key = f"blog-output-{current_time}.txt"
            s3_bucket = "awsbedrockdhanu"
            save_blog_details_in_s3(s3_key, s3_bucket, blog_content)
            message = "Blog generated and saved to S3."
        else:
            message = "No blog was generated."

        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }

    except Exception as e:
        print(f"Error in lambda_handler: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Internal error: {e}")
        }
