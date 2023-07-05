from os import listdir
import soundfile as sf

"""
This program convert an audio file to wav.
"""

src_folder = "conversion_src/"
dest_folder = "conversion_dest/"

files_in_audios_folder = listdir(src_folder)

for audio_path in files_in_audios_folder:
    audio, sample_rate = sf.read(src_folder+audio_path)
    sf.write(f"{dest_folder}{audio_path[:-4]}.wav", audio, sample_rate)
