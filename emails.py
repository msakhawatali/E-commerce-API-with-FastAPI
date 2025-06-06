from fastapi import BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from pydantic import BaseModel, EmailStr
from typing import List
from models import User
import jwt

# Load .env credentials
config_credentials = dotenv_values(".env")

# ✅ FastAPI-Mail config
conf = ConnectionConfig(
    MAIL_USERNAME=config_credentials["EMAIL"],
    MAIL_PASSWORD=config_credentials["PASS"],
    MAIL_FROM=config_credentials["EMAIL"],
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

# ✅ Schema for validating list of emails
class EmailSchema(BaseModel):
    email: List[EmailStr]


# ✅ Send email function
async def send_email(email: List[str], instance: User):
    # Create JWT token
    token_data = {
        "id": instance.id,
        "username": instance.username
    }

    token = jwt.encode(token_data, config_credentials["SECRET"], algorithm="HS256")

    # ✅ Fixed typos in HTML and style attributes
    template = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset="UTF-8">
            </head>
            <body>
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column;">
                    <h3>Account Verification</h3>
                    <br>
                    <p>Thanks for choosing EasyShopas. Please click the button below to verify your account:</p>
                    <a style="margin-top: 1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;" href="http://localhost:8000/verification/?token={token}">
                        Verify your email
                    </a>
                    <p>Please ignore this email if you did not register for EasyShopas. Nothing will happen. Thanks!</p>
                </div>
            </body>
        </html>
    """

    # ✅ MessageSchema with HTML body
    message = MessageSchema(
        subject="EasyShopas Account Verification Email",
        recipients=email,
        body=template,
        subtype="html"
    )

    # Send the email
    fm = FastMail(conf)
    await fm.send_message(message=message)
