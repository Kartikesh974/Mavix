import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings

def send_enquiry_email(name: str, email: str, message: str) -> bool:
    """Send enquiry details to company email using SMTP."""
    try:
        msg = MIMEMultipart()
        msg["From"] = settings.SMTP_USER
        msg["To"] = settings.EMAIL_RECIPIENT
        msg["Subject"] = f"New Enquiry from {name}"

        body = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False