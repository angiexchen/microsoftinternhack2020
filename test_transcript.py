from youtube_transcript_api import YouTubeTranscriptApi

t1 = YouTubeTranscriptApi.get_transcript("LvgcfMOyREE")

print("Hello")
def get_closest_less_than_or_equal(transcript, time): 
    text = ""
    minVal = 100000
    minIndex = 0
    print(transcript)
    print(transcript[0])
    print(transcript[0]['start'])
    for i in range(0,len(transcript)):
        item = transcript[i] 
        if item["start"] < time/2 and time/2 - item["start"] < minVal:
            minVal = time/2 - item["start"]
            print(item["start"])
            minIndex = i
        print(minVal)
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
     print("reached")
     print(s)
     print(e)
     for i in range(s, e):
         text += transcript[i]["text"]
         print(i)
         print(transcript[i]["text"])
     return text

print(get_closest_less_than_or_equal(t1,100))