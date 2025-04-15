# 🧠 Serverless Blog Generator using Meta’s LLaMA 3 on AWS with GenAI
This project demonstrates how to build a **serverless blog generator** that leverages **Meta's LLaMA 3 (70B Instruct)** model via **Amazon Bedrock**, powered by **AWS Lambda**, **API Gateway**, and **Amazon S3**.

Whenever a blog topic is sent via an API call (e.g., from Postman), the system generates a blog using the LLaMA 3 model and stores the result as a `.txt` file in an S3 bucket.

---

## 🚀 Tech Stack

- **🧠 Meta LLaMA 3 70B (via Amazon Bedrock)**
- **🐍 Python (3.9+)**
- **🟡 AWS Lambda**
- **🌐 Amazon API Gateway**
- **📂 Amazon S3**
- **🧪 Postman (for API testing)**

---

## 🧩 Architecture Overview
Postman (blog_topic) ⬇ Amazon API Gateway (POST API) ⬇ AWS Lambda Function (Python) ⬇ Amazon Bedrock (Meta LLaMA 3 Model) ⬇ Generated Blog Content ⬇ Amazon S3 (.txt File Storage)

## 📦 How It Works

1. 🔗 Send a POST request via **Postman** with the blog topic:
   ```json
   {
     "blog_topic": "The Future of AI in Healthcare"
   }
2. 🔁 The API Gateway triggers the Lambda function.
3. 🧠 The Lambda function sends the blog topic to the LLaMA 3 70B model using the Bedrock runtime.
4. 📝 The model returns the generated blog content.
5. 💾 The blog is saved as a .txt file in your specified S3 bucket.

## 🔧 Lambda Function Key Snippet
```json
response = bedrock.invoke_model(
    modelId="meta.llama3-70b-instruct-v1:0",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({
        "prompt": f"Write a blog of 200 words on the topic: {blogtopic}",
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    })
)
```
## 🧪 Sample API Request (Postman)
- Endpoint: POST https://01jdl2g89k.execute-api.us-east-1.amazonaws.com/dev/Blog-generation
- Headers:
    - Content-Type: application/json
- Body:
```json
{
  "blog_topic": "The Role of Generative AI in Modern Education"
}
```
## ✅ Prerequisites
- An AWS account with access to:
    - Bedrock + LLaMA 3 model
    - Lambda
    - S3
    - API Gateway
    - Postman
## 🧬 Clone & Deploy from GitHub
You can clone the entire Lambda function setup from this GitHub repository and deploy it within your AWS account.
🔗 GitHub Repo:https://github.com/DhanushGD/BLOG-GENERATOR.git
🚀 To Use:
```bash
# 1. Clone the repo
git clone https://github.com/yourusername/serverless-llama3-blog-generator.git

# 2. Navigate into the project
cd serverless-llama3-blog-generator

# 3. Zip the Lambda function code
zip function.zip lambda_function.py

# 4. Upload the zip to your Lambda function in AWS Console or use AWS CLI
🧠 Note: Ensure your Lambda is set up with proper IAM permissions to access AWS Bedrock,lambda,APIGateway and S3.

# 5. Create a API endpoint and route in APIGateway and send the request through postman
```

## 📸 Screenshots 
You can include:
📥 Postman request example
![image](https://github.com/user-attachments/assets/9d64f25e-1ade-4576-b4e4-a68d90f78f21)

🛠️ Lambda setup
![image](https://github.com/user-attachments/assets/b0fbfef2-5467-4fdf-a2da-6fa6348bc6d3)

🔗 API Gateway configuration
![image](https://github.com/user-attachments/assets/5c7bd8a8-f4e4-493b-b7fd-91aead828bd0)

![image](https://github.com/user-attachments/assets/fbfcd4a8-97b4-4e28-a71c-54a1c26e2ca3)

📁 S3 bucket with saved blog files
![image](https://github.com/user-attachments/assets/ffed4518-076f-4313-8b94-27b9932f4352)

Response txt file from s3 - [blog-output-20250414070032.txt](blog-output-20250414070032.txt)

## 📌 Use Cases
- Blog generation apps
- Content creation automation
- GenAI proof-of-concepts
- Serverless AI workflows
