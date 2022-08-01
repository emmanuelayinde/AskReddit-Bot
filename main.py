from datetime import date
import os
from os import path as checkpath
import shutil
import time
from reddit import generate_askreddit_q_a
from upload_video import upload_video




path = os.getcwd()
generated_path =  path + "\\generated"

title = ''

    
# Leave if you want to run it 24/7
while True:
 
    
    if checkpath.exists(generated_path):
        shutil.rmtree(generated_path, ignore_errors=True, onerror=None)
    else:
        print('path does not exist...........................')
  
 
    # latest_askreddit = reddit.subreddit('AskReddit').hot(limit=1) 

    def GetDaySuffix(day):
        if day == 1 or day == 21 or day == 31:
            return "st"
        elif day == 2 or day == 22:
            return "nd"
        elif day == 3 or day == 23:
            return "rd"
        else:
            return "th"



    # Wanted a date in my titles so added this helper
    DAY = date.today().strftime("%d")
    DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    dt_string = date.today().strftime("%A %B") + f" {DAY}"

    print('Starting video creation....................#########################################')

    time.sleep(1)  

    # Create the video itself!
    generate_askreddit_q_a()

    time.sleep(2)  

    print('Done with creating video....................#########################################')

    with open(path+"\\temp\\used.txt") as file:
        for line in file:
            pass
        title = line


    title = title.split('\n')[0]

    video_data = {
            "file": f"{path}/generated/finalVideos/final/finalVideo.mp4",
            "title": f"{title} - AskReddit question and answer {dt_string}!",
            "description": "#shorts\nGiving you the hottest questions of the day with funny comments!",
            "keywords": "AskReddit,redditquestion,questionandanswer",
            "privacyStatus": "public",
    }

    print(video_data)
    print("Posting Video in 2 minutes..............................###########################################")
    time.sleep(2)
    upload_video(video_data)

    print('Done..........................................................@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#########################################')

    # Sleep until ready to post another video!
    time.sleep(60 * 60 * 6)
