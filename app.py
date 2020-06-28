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
        t1 = YouTubeTranscriptApi.get_transcript(videoId)
        print(type(t1))
        t2 = t1[0]
        print(type(t2))

        testlist = ["one", "two", "three"]
        
        return render_template('response.html', message = t1, testlist = testlist)


# def get_text(start, end, transcript):
#     s = get_closest(start, transcript)
#     e = get_closest(end, transcript)
#     text = ''
#     for i in range(s, e):
#         text += transcript[i]["text"]
#     return text

# def get_closest(time, transcript, startIdx):
#     if time < transcript[startIdx]["start"]:
#         return "ERROR!"
    



        
