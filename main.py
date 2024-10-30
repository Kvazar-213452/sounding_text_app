from flask import Flask, Response
from head_com.shell import start_shell
import sys

app = Flask(__name__)

start_shell()

@app.route("/")
def index():
    html_content = """
    <html>
        <body>
            <h1>Ласкаво просимо до Flask-сервера!</h1>
        </body>
    </html>
    """
    return Response(html_content, mimetype="text/html")

if __name__ == "__main__":
    try:
        app.run(port=5000)
    except KeyboardInterrupt:
        sys.exit(0)
