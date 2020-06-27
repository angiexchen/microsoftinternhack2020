import os
from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv()

COGSVCS_KEY = os.getenv('COGSVCS_KEY')
COGSVCS_CLIENTURL = os.getenv('COGSVS_CLIENTURL')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    
