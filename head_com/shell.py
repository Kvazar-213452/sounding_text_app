import subprocess
import os
import threading
import time
import signal

def start_shell():
    executable_path = os.path.join(os.getcwd(), "core", "shell_web.exe")
    args = ["sorse", "400", "400", "<style>iframe{position: fixed;height: 100%;width: 100%;top: 0%;left: 0%;}</style><iframe src='http://127.0.0.1:5000/' frameborder='0'></iframe>"]

    process = subprocess.Popen([executable_path] + args, cwd=os.path.join(os.getcwd(), "core"))

    def monitor_process():
        while True:
            if process.poll() is not None:
                os.kill(os.getpid(), signal.SIGINT)
                break
            time.sleep(1)

    monitor_thread = threading.Thread(target=monitor_process)
    monitor_thread.start()