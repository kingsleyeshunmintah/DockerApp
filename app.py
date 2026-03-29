from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Eshun Kingsley Mintah - UEB3221622</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f5f5f5;
                }
                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    background-color: white;
                    padding: 40px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    text-align: center;
                }
                h1 {
                    color: #333;
                    margin-bottom: 10px;
                }
                .info-box {
                    background-color: #f9f9f9;
                    border-left: 4px solid #007bff;
                    padding: 20px;
                    margin: 20px 0;
                    text-align: left;
                }
                .info-box p {
                    margin: 8px 0;
                    color: #555;
                }
                .status {
                    background-color: #d4edda;
                    color: #155724;
                    padding: 15px;
                    border-radius: 4px;
                    margin-top: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Modern Trends in Tech</h1>
                <div class="info-box">
                    <p><strong>Name:</strong> Eshun Kingsley Mintah</p>
                    <p><strong>Index Number:</strong> UEB3221622</p>
                    <p><strong>Project:</strong> Docker Application</p>
                </div>
                <div class="status">
                    ✓ This Python application is running inside a Docker Container!
                </div>
            </div>
        </body>
    </html>
    """

if __name__ == '__main__':
    # It's important to set host to 0.0.0.0 to be accessible outside the container
    app.run(host='0.0.0.0', port=5000)