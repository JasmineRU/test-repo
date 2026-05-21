import googleapiclient.discovery
import pandas as pd
my_API_KEY = "AIzaSyDc9buo6M2K-imhAmYw0eNsuRPPg4W_iEY"
api_service_name = "youtube"
api_version = "v3"

#Enter and assign developer key to variable

youtube = googleapiclient.discovery.build(

        api_service_name, api_version, developerKey = my_API_KEY)

def youtubeSearch(question):
    
    request = youtube.search().list(

        part="id,snippet",

        type='video',

        q=question,

        videoDuration='short',

        videoDefinition='high',

        maxResults=1

    )

# Request execution

    response = request.execute()

    print(response)

youtubeSearch("Fleetwood Mac")
print()
youtubeSearch("Maroon 5")
print()
youtubeSearch("Michael Jackson")
