import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

COGSVCS_KEY = os.getenv('COGSVCS_KEY')
COGSVCS_CLIENTURL = os.getenv('COGSVS_CLIENTURL')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        YouTubeTranscriptApi.get_transcript('hCOIMkcsm_g')
        transcript_list = YouTubeTranscriptApi.list_transcripts('hCOIMkcsm_g', languages=['de', 'en'])
        transcript = transcript_list.find_generated_transcript(['de', 'en'])
        return render_template('form.html')
