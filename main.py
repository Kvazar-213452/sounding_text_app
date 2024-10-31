from flask import Flask, render_template, jsonify, request
from head_com.shell import run_shell_web, load_config, save_config
from head_com.audio import play_audio
import threading

app = Flask(__name__)

config = load_config('config.json')

server_thread = None
PORT = config.get('port')
config_path = '../config.json'

@app.route('/')
def index():
    return render_template("index.html") 

@app.route('/send', methods=['POST'])
def receive_input():
    config = load_config(config_path)
    index_audio = config.get('index_audio')
    lang = config.get('lang')

    data = request.get_json()
    input_value = data.get('input')

    play_audio(input_value, index_audio, lang)

    return jsonify({"status": "success"})

@app.route('/get_index', methods=['POST'])
def get_data():
    config = load_config(config_path)
    index_audio = config.get('index_audio')

    return jsonify({"index": index_audio})

@app.route('/get_lang', methods=['POST'])
def get_data1():
    config = load_config(config_path)
    lang = config.get('lang')

    return jsonify({"index": lang})

@app.route('/index_change', methods=['POST'])
def index_change():
    data = request.get_json()
    input_value = data.get('input')

    config = load_config(config_path)

    config['index_audio'] = int(input_value)

    save_config(config_path, config)

    return jsonify({"status": "success"})

@app.route('/lang_change', methods=['POST'])
def index_change1():
    data = request.get_json()
    input_value = data.get('input')

    config = load_config(config_path)

    config['lang'] = str(input_value)

    save_config(config_path, config)

    return jsonify({"status": "success"})

def run_flask_app():
    app.run(port=PORT)

if __name__ == '__main__':
    server_thread = threading.Thread(target=run_flask_app)
    server_thread.start()
    
    run_shell_web(PORT)