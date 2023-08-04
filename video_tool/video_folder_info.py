import os
from moviepy.editor import VideoFileClip
from datetime import datetime


class VideoFolderInfo:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def video_info(self):
        video_info_list = []

        for file_name in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, file_name)

            if os.path.isfile(file_path):
                try:
                    video = VideoFileClip(file_path)
                    name, file_extension = os.path.splitext(file_name)
                    duration = video.duration
                    location = file_path
                    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    video_info = {
                        "clip_name": name,
                        "clip_file_extension": file_extension,
                        "clip_duration": duration,
                        "clip_location": location,
                        "insert_timestamp": time
                    }
                    video_info_list.append(video_info)
                    video.close()
                except Exception as e:
                    print(f"Error al procesar el archivo {file_name}: {e}")

        return video_info_list


# Uso de la clase para obtener información de videos en una carpeta
if __name__ == "__main__":
    folder_path = r"C:\Users\Lucer\Desktop\Python\video_clips"
    video_folder = VideoFolderInfo(folder_path)
    video_info_list = video_folder.video_info()

    for video_info in video_info_list:
        #a.insert_data(video_info)
        print(video_info)
