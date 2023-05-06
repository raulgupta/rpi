from flask import Flask
import os
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/run-script', methods=['POST'])
def run_script():
    script_path = '/home/stratas/script.py'  # Change this to the path of your script
    subprocess.call(['python3', script_path])
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
