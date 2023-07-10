from pydub import AudioSegment
from pydub.utils import make_chunks
from os import listdir, getcwd, path
from choose_folder import choose_folder_from_path

def divide_audios_in_folder(folder_path: str=getcwd(), size: float=1) -> list:
    """
    Divides all the .wav audios in the folder_path into parts that have {size} seconds.\n
    Default folder is the current folder, default size is 1 second.
    Returns a list with all divided audios.\n
    """
    divided_audios = []

    audio_files = listdir(folder_path)

    size = size*1000 #miliseconds

    for audio_path in audio_files:
        file_name, extesion = path.splitext(audio_path)
        
        if extesion != '.wav': continue

        audio = AudioSegment.from_file(path.join(folder_path, audio_path), 'wav')

        parts = make_chunks(audio, size)
        for i, part in enumerate(parts):
            part_name = f'{path.join(folder_path, file_name)}_{i}.wav'
            part.export(part_name, format='wav')

        divided_audios.append(path.join(folder_path,audio_path))
    
    return divided_audios

if __name__ == "__main__":
    divide_audios_in_folder(choose_folder_from_path(), float(input('Audio size (seconds): ')))