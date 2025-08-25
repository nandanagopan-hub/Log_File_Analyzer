import re
import configparser
import html_creation
from Email_Notifier import Email_Notifier

config = configparser.ConfigParser()
config.read('config.ini')
test_data = config['test_data']['test_data']
sender_email = config['email']['sender_email']
sender_password = config['email']['sender_password']
recipient_email = config['email']['recipient_email']

def test_analyze_logs(log_file):
    errors=[]
    warnings=[]
    print("Analyzing logs...")
    with open(log_file,"r") as log_open:
        for line in log_open:   
            if(re.search(r'ERR+',line)):
                errors.append(line.strip())
            if(re.search(r'WARN+',line)):
                warnings.append(line.strip())
    assert len(errors) > 0, "No errors found in logs"
    assert len(warnings) > 0, "No warnings found in logs"
    with open(test_data,"w") as error_file:
        error_file.write(f"ERRORS:\nFound {len(errors)} errors in logs")
        for error in errors:
            error_file.write(error + "\n")
        error_file.write(f"WARNINGS:\nFound {len(warnings)} warnings in logs")
        for warning in warnings:
            error_file.write(warning + "\n")
    print("Logs analyzed successfully")
    print("Path to Error Analysis: Logs/Errors_Analysis.txt")
    #Create the HTML report
    html_report_path= html_creation.html_creation(test_data)
    if html_report_path:
        print(f"HTML Report Path: {html_report_path}")   
    email_obj=Email_Notifier(sender_email, sender_password, recipient_email) 
    email_obj.send_error_analysis_email(html_report_path)    
