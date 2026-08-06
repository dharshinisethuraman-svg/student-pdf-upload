# Student PDF Upload System (AWS)
A serverless web application that allows users to upload PDF files securely to cloud storage using pre-signed URLs.

## 🚀 Technologies Used
- AWS S3 (Object Storage)
- AWS Lambda (Serverless Backend)
- API Gateway (REST API)
- HTML, JavaScript (Frontend)

## ✨ Features
- Secure file upload using pre-signed URLs
- Serverless architecture (no backend server needed)
- CORS handling for browser-based uploads
- Direct upload to S3 without exposing credentials

## ⚙️ How It Works
1. User selects a PDF file in the browser
2. Frontend sends request to API Gateway
3. Lambda function generates a pre-signed URL
4. File is uploaded directly to S3 using the URL

## 📂 Output
- Uploaded PDF files are stored in S3 bucket
- Files can be accessed using object URLs

## 📌 Key Learnings
- Implemented secure file upload using AWS
- Understood CORS and browser security policies
- Worked with serverless architecture
- Debugged real-world integration issues

## Development & Debugging

![API Gateway Routes](screenshots/api-gateway-routes.png)
*Configured the /upload POST route in API Gateway*

![Testing with Hoppscotch](screenshots/hoppscotch-test.png)
*Tested the endpoint using Hoppscotch before connecting the frontend*

![CORS Error Debugging](screenshots/cors-error.png)
*Encountered and resolved CORS policy errors by adding proper Access-Control-Allow-Origin headers in the API response*

## Note: Live AWS resources were taken down after the free tier period to avoid unexpected charges. The Lambda function above was recreated post-teardown to match the original logic and is included here as reference.

## 👩‍💻 Author
Dharshini SR
