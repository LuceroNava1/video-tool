import os
from moviepy.editor import VideoFileClip


class CreateVideos:
    def create_clips(video_path):
        output_folder = "video_clips"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        video = VideoFileClip(video_path)
        total_duration = video.duration
        clip_duration_secs = 60
        num_clips = int(total_duration / clip_duration_secs)

        for i in range(num_clips):
            start_time = i * clip_duration_secs
            end_time = start_time + clip_duration_secs
            clip = video.subclip(start_time, end_time)
            initial_frame = int(start_time * video.fps)
            clip_filename = os.path.join(output_folder, f"{initial_frame}thFrame.mp4")
            clip.write_videofile(clip_filename, codec="libx264")
        video.close()

if __name__ == "__main__":
    # ffmpeg, moviepy needed
    video_path = r'C:\Users\...\...\...\airshow.mp4'
    create_clips(video_path)