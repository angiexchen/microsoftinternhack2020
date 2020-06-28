import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from image_processing_library import get_images
import re 

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
        images = get_images()
        result = []
        start_text = get_text(0, extract_int_from_file_extension(images[0]), t1)
        obj = JinjaTemplateObject('data/frame0.jpg',  start_text)
        result.append(obj)
        for i in range(len(images)-1):
            start = extract_int_from_file_extension(images[i])
            if start == -1:
                continue 
            end = extract_int_from_file_extension(images[i+1])-1
            if end == -1:
                continue 
            text = get_text(start, end, t1)
            if i == len(images): 
                end_text = get_text(end, len(t1) - 1, t1)
                obj = JinjaTemplateObject(images[i], text + end_text)
            else: 
                obj = JinjaTemplateObject(images[i], text)
            result.append(obj)
        testlist = ["one", "two", "three"]
        
        return render_template('response.html', message = t1, testlist = testlist, images=result)

def get_closest_less_than_or_equal(transcript, time): 
    text = ""
    minVal = 10000
    minIndex = 0
    for i in range(0,len(transcript)):
        item = transcript[i] 
        if item["start"] < time/2 and abs(time/2 - int(item["start"])) < minVal:
            minVal = abs(time/2 - int(item["start"]))
            minIndex = i
    return minIndex

def extract_int_from_file_extension(test_string):
    temp = re.findall(r'\d+', test_string) 
    res = list(map(int, temp)) 
    if len(res) != 0:
        return res[0]
    else: 
        return -1

def get_text(start, end, transcript):
     s = get_closest_less_than_or_equal(transcript, start)
     e = get_closest_less_than_or_equal(transcript, end)
     text = ''
     if (s == e):
         return transcript[s]["text"]
     for i in range(s, e):
         text += ' ' + transcript[i]["text"] + ' '
     return text

class JinjaTemplateObject(): 
    def __init__(self, image_file, text):
        self.image_file = image_file
        self.text = text 

# def get_closest(time, transcript, startIdx):
#     if time < transcript[startIdx]["start"]:
#         return "ERROR!"
    
if __name__ == "__main__":
    app.run(debug=True)


        
