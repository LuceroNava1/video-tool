from video_tool.data_base import DataBase
from video_tool.video_folder_info import  VideoFolderInfo
from video_tool.create_videos import CreateVideos

video_path = r'C:\Users\Lucer\Documents\Github\proyectos\videoTool\airshow.mp4'
CreateVideos.create_clips(video_path)

db = DataBase()
db.connect()
db.create_table()

folder_path = r"C:\Users\Lucer\Documents\Github\proyectos\videoTool\video_clips"
video_folder = VideoFolderInfo(folder_path)

video_info_list = video_folder.video_info()
for video_info in video_info_list:
    db.insert_data(video_info)
    print(video_info)

db.create_csv()
if __name__ == '__main__':
    print('Done')

