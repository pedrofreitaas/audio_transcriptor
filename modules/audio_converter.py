from os import listdir, scandir, DirEntry
import soundfile as sf
from choose_folder import choose_folder_from_path

def convert_audios_in_folder(folder_path: str) -> list[str]:
    """
    Converts all the .mp3 into .wav's.\n
    Returns a list containing the paths to all converted files.\n
    """
    conv_audios = []
    files_in_audios_folder = listdir(folder_path)

    for audio_path in files_in_audios_folder:
        if audio_path[-4:] != '.mp3': continue
        
        audio, sample_rate = sf.read(folder_path+audio_path)
        sf.write(f"{folder_path}{audio_path[:-4]}.wav", audio, sample_rate)

        conv_audios.append(folder_path+audio_path)

    return conv_audios

if __name__ == '__main__':
    convert_audios_in_folder(choose_folder_from_path())