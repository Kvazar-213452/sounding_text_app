import subprocess
import os

def run_shell_web(port):
    os.chdir('core')
    html_code = "<style>iframe{{position: fixed;height: 100%;width: 100%;top: 0%;left: 0%;}}</style><iframe src='http://127.0.0.1:{}/' frameborder='0'></iframe>".format(port)
    command = [
        "shell_web.exe",
        "sorse", 
        str(400), 
        str(400),
        html_code
    ]

    process = subprocess.Popen(command)

    process.wait()

    os._exit(0)