import os
import psycopg2
import os
import csv
from moviepy.editor import VideoFileClip
from datetime import datetime
from video_tool import *

video_path = r'C:\Users\...\...\...\...\videoTool\airshow.mp4'
create_videos.CreateVideos.create_clips(video_path)

db = DataBase()
db.connect()
db.create_table()

folder_path = r"C:\Users\...\...\...\video_clips"
video_folder = VideoFolderInfo(folder_path)

video_info_list = video_folder.video_info()
    for video_info in video_info_list:
        db.insert_data(video_info)
        print(video_info)

db.create_csv()
if __name__ == '__main__':
    print('Hi')

