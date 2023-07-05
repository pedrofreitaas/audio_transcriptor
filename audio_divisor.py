from pydub import AudioSegment
from pydub.utils import make_chunks
from os import listdir

src_folder = "division_src/"
dest_folder = "division_dest/"

audio_files = listdir(src_folder)

size_in_seconds = 60 #seconds
size = size_in_seconds*1000 #miliseconds

for audio_path in audio_files:
    audio = AudioSegment.from_file(src_folder+audio_path, 'wav')

    partes = make_chunks(audio, size)
    for i, parte in enumerate(partes):
        parte_name = f'{dest_folder}{audio_path[:-4]}_{i}.wav'
        parte.export(parte_name, format='wav')