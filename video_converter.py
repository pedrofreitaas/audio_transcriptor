from moviepy.editor import *
from os import listdir

""""
This short program converts video (mp4) to sounds (mp3).
"""

def convert_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    video.audio.write_audiofile(mp3_file, codec='mp3')

src_folder = "videos_src"
dest_folder = "videos_dest"

mp4_files = listdir(src_folder)

for video_path in mp4_files:
    convert_to_mp3(src_folder+"/"+video_path, f"{dest_folder}/{video_path[:-4]}.mp3")
