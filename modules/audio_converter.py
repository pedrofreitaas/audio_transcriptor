from os import listdir, getcwd, path
import soundfile as sf
from choose_folder import choose_folder_from_path

def convert_audios_in_folder(folder_path: str=getcwd()) -> list[str]:
    """
    Converts all the .mp3 into .wav's.\n
    Default source path and destiny folder are the current dir.\n
    Returns a list containing the paths to all converted files.\n
    """
    conv_audios = []
    files_in_audios_folder = listdir(folder_path)

    for audio_path in files_in_audios_folder:
        file_name, extension = path.splitext(audio_path)
        
        if extension != '.mp3': continue
        
        final_path = path.join(folder_path, audio_path)

        audio, sample_rate = sf.read(final_path)
        sf.write(path.join(folder_path,file_name)+".wav", audio, sample_rate)

        conv_audios.append( path.join(folder_path, audio_path) )

    return conv_audios

if __name__ == '__main__':
    convert_audios_in_folder(choose_folder_from_path())