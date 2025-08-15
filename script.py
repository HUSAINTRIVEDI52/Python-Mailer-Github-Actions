import smtplib
from email.mime.text import MIMEText #mimetext is a class that represents the texts of the email
from email.mime.multipart import MIMEMultipart #MIMEMultipart is a class that represemts the email message
import os


def send_mail(workflow_name,repo_name,workflow_run_id):
    #Email details
    sender_email=os.getenv('SENDER_EMAIL')
    sender_password=os.getenv('SENDER_PASSWORD')
    receiver_email=os.getenv('RECEIVER_EMAIL')

    #EMAIL MESSEGE
    subject=f"Workflow {workflow_name} failed for repo{repo_name}"
    body=f"Hi,the workflow {workflow_name} failed for the repo {repo_name}.Please check the logs for more inffo.\nMore Details.\nRun_id:{workflow_run_id}"


    msg=MIMEMultipart()
    msg['From'] =sender_email
    msg['To']=receiver_email
    msg['subject']=subject
    msg.attach(MIMEText(body,'plain'))

    try:
        server = smtplib.SMTP(smtp.gmail.com,587)
        server.starttls()
        server.login(sender_email,sender_password)
        text = msg._as_string()
        server.sendmail(sender_email,receiver_email,text)
        server.quit()

        print('Email sent successfully')
    except Exception as e:
        print(f'Error: {e}')


send_mail(os.getenv('WORKFLOW_NAME'),os.getenv('REPO_NAME'),os.getenv('WORKFLOW_RUN_ID'))
