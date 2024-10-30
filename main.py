from flask import Flask, render_template, jsonify, request
from head_com.shell import run_shell_web
from head_com.audio import play_audio
import threading

app = Flask(__name__)

PORT = 4000
server_thread = None

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/send', methods=['POST'])
def receive_input():
    data = request.get_json()
    input_value = data.get('input')
    play_audio(input_value)
    return jsonify({"status": "success"})

def run_flask_app():
    app.run(port=PORT)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_flask_app)
    server_thread.start()
    
    run_shell_web(PORT)