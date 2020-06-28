import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()

COGSVCS_KEY = os.getenv('COGSVCS_KEY')
COGSVCS_CLIENTURL = os.getenv('COGSVS_CLIENTURL')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        url = request.form.get("link")
        # Find the video ID from the URL
        startIdx = url.find('=')
        endIndx = url.find('&')
        if not (startIdx == -1 & endIndx == -1):
            videoId = url[startIdx + 1: endIndx]
        else: 
            return render_template('error.html', message = "Invalid YouTube URL entered.")
        YouTubeTranscriptApi.get_transcript(videoId)
        transcript_list = YouTubeTranscriptApi.list_transcripts(videoId)
        transcript = transcript_list.find_generated_transcript(['de', 'en'])
        print(transcript_list)
        print("\n\n")
        print(transcript)
        return render_template('response.html', message = videoId)
    

        
