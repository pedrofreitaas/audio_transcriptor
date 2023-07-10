from moviepy.video.io.VideoFileClip import VideoFileClip
from os import listdir, getcwd, path
if __name__ != "__main__": from modules.choose_folder import choose_folder_from_path
else: from choose_folder import *

def convert_to_mp3(mp4_file: str, mp3_file: str) -> None:
    """
    Converts video (mp4) to sound (mp3).\n
    Saves the .mp3 file.\n
    """
    video = VideoFileClip(mp4_file)
    video.audio.write_audiofile(mp3_file, codec='mp3')

def convert_videos_in_folder(folder_path: str=getcwd()) -> list[str]:
    """
    Converts all videos (.mp4) from the folder into audios (mp3).\n
    Returns a list with the result's paths.\n
    """
    mp4_files = listdir(folder_path)

    conversions = []

    for video_path in mp4_files:
        file_name, extension = path.splitext(video_path)

        if extension != ".mp4": continue

        convert_to_mp3(path.join(folder_path, video_path), path.join(folder_path, file_name+".mp3"))

        conversions.append(path.join(folder_path, file_name+".mp3"))

    return conversions

if __name__ == '__main__':
    convert_videos_in_folder(choose_folder_from_path())