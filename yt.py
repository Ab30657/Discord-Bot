from googleapiclient.discovery import build
import os
#---------------------------------------
#Youtube API----------------------------
#---------------------------------------

def get_subcount():
  youtube = build('youtube', 'v3',developerKey=os.getenv('YT_API_KEY'))
  _req=youtube.channels().list(
  part='statistics',
  id='UC2e8r3D4hXZWVhkFJGpL7QQ'
  )
  return (_req.execute())['items'][0]['statistics']['subscriberCount']
#---------------------------------------

  