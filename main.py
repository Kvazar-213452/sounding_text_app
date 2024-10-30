from flask import Flask, render_template
from head_com.shell import run_shell_web
import threading

app = Flask(__name__)

PORT = 4000
server_thread = None

@app.route('/')
def index():
    return render_template("index.html") 

def run_flask_app():
    app.run(port=PORT)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_flask_app)
    server_thread.start()
    
    run_shell_web(PORT)