from pydub import AudioSegment
from pydub.utils import make_chunks
from os import listdir

def divide_audios_in_folder(folder_path: str, size: float) -> list:
    """
    Divides all the audios in the folder into parts that have {size} seconds.\n
    Returns the list of divided audios.\n
    """
    divided_audios = []

    audio_files = listdir(folder_path)

    size = size*1000 #miliseconds

    for audio_path in audio_files:
        if audio_path[-4:] != '.wav': continue

        audio = AudioSegment.from_file(folder_path+audio_path, 'wav')

        partes = make_chunks(audio, size)
        for i, parte in enumerate(partes):
            parte_name = f'{folder_path}{audio_path[:-4]}_{i}.wav'
            parte.export(parte_name, format='wav')

        divided_audios.append(folder_path+audio_path)
    
    return divided_audios