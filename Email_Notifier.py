import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import configparser

class Email_Notifier:
    def __init__(self, sender_email, sender_password, recipient_email, smtp_server="smtp.gmail.com", smtp_port=587):
        """
        Initialize Email_Notifier with email credentials
        
        Args:
            sender_email (str): Sender's email address
            sender_password (str): Sender's password or app password
            recipient_email (str): Recipient's email address
            smtp_server (str): SMTP server (default: smtp.gmail.com)
            smtp_port (int): SMTP port (default: 587)
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def send_error_analysis_email(self, html_report_path):
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_email
            msg['Subject'] = "Log File Analysis - Errors and Warnings Report"
            
            # Email body
            body = """
Hello,

Please find the Error and Warnings Analysis of the log file shared to Log_file_Analyzer.

Best regards,
Log File Analyzer System
            """
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach the HTML file
            if os.path.exists(html_report_path):
                with open(html_report_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= {os.path.basename(html_report_path)}'
                )
                msg.attach(part)
                print(f"HTML file attached: {html_report_path}")
            else:
                print(f"Warning: {html_report_path} not found")
                return False
            
            # Send email
            print("Connecting to SMTP server...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            text = msg.as_string()
            server.sendmail(self.sender_email, self.recipient_email, text)
            server.quit()          
            print("✅ Email sent successfully!")
            return True
            
        except smtplib.SMTPAuthenticationError:
            print("❌ Authentication failed. Please check your email and password.")
            return False
        except smtplib.SMTPException as e:
            print(f"❌ SMTP error occurred: {e}")
            return False
        except Exception as e:
            print(f"❌ Error sending email: {e}")
            return False

