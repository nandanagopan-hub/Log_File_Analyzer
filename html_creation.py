import os

def html_creation(test_data):
    """
    Create an HTML page from Error_Analysis.txt
    """
    try:
        # Define the HTML output path
        html_report_path = "Logs/Errors_Analysis.html"
        
        # Read the text file
        with open(test_data, "r") as txt_file:
            lines = txt_file.readlines()
        
        # Create HTML content
        html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log Error Analysis Report</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            border-bottom: 3px solid #007bff;
            padding-bottom: 10px;
        }
        h2 {
            color: #007bff;
            margin-top: 30px;
            border-left: 4px solid #007bff;
            padding-left: 15px;
        }
        .error-section {
            background-color: #fff5f5;
            border: 1px solid #ffcdd2;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        .warning-section {
            background-color: #fffbf0;
            border: 1px solid #ffeaa7;
            border-radius: 5px;
            padding: 15px;
            margin: 10px 0;
        }
        .log-entry {
            background-color: #f8f9fa;
            border-left: 3px solid #007bff;
            padding: 8px 12px;
            margin: 5px 0;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            word-wrap: break-word;
        }
        .summary {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
            border-left: 4px solid #2196f3;
        }
        .timestamp {
            text-align: center;
            color: #666;
            font-style: italic;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Log Error Analysis Report</h1>
        <div class="timestamp">Generated on: """ + str(__import__('datetime').datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + """</div>
"""
        
        # Process the content
        current_section = None
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith("ERRORS:"):
                current_section = "errors"
                html_content += f'<div class="error-section">\n<h2>🔴 {line}</h2>\n'
            elif line.startswith("WARNINGS:"):
                if current_section == "errors":
                    html_content += '</div>\n'
                current_section = "warnings"
                html_content += f'<div class="warning-section">\n<h2>🟡 {line}</h2>\n'
            elif line.startswith("Found ") and ("errors" in line or "warnings" in line):
                html_content += f'<div class="summary"><strong>{line}</strong></div>\n'
            else:
                if line:
                    html_content += f'<div class="log-entry">{line}</div>\n'
        
        # Close any open sections
        if current_section:
            html_content += '</div>\n'
        
        # Close HTML
        html_content += """
    </div>
</body>
</html>
"""
        
        # Write the HTML file
        with open(html_report_path, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        
        print(f"HTML report generated successfully at: {html_report_path}")
        return html_report_path
        
    except Exception as e:
        print(f"Error generating HTML report: {e}")
        return None

# Global variable for the HTML report path
html_report_path = "Logs/Errors_Analysis.html"
html_report = "Errors_Analysis.html" 