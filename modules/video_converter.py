from moviepy.video.io.VideoFileClip import VideoFileClip
from os import listdir, scandir, DirEntry, getcwd, path
from choose_folder import choose_folder_from_path

def convert_to_mp3(mp4_file: str, mp3_file: str) -> None:
    """
    Converts video (mp4) to sound (mp3).\n
    Saves the .mp3 file.\n
    """
    video = VideoFileClip(mp4_file)
    video.audio.write_audiofile(mp3_file, codec='mp3')

def convert_videos_in_folder(folder_path: str=getcwd()) -> None:
    """Converts all videos (.mp4) from the folder into audios (mp3).\n"""
    mp4_files = listdir(folder_path)

    for video_path in mp4_files:
        file_name, extesion = path.splitext(video_path)

        if extesion != ".mp4": continue

        convert_to_mp3(path.join(folder_path, video_path), path.join(folder_path, file_name+".mp3"))

if __name__ == '__main__':
    convert_videos_in_folder(choose_folder_from_path())