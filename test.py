from youtube_transcript_api import YouTubeTranscriptApi

t1 = YouTubeTranscriptApi.get_transcript('hCOIMkcsm_g')
transcript_list = YouTubeTranscriptApi.list_transcripts('hCOIMkcsm_g')
transcript = transcript_list.find_generated_transcript(['de', 'en'])
print(t1)