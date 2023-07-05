import speech_recognition as sr
from os import listdir

"""
This program takes all audio inputs in the transcriptor_src
and transcribes then into the file: "transcript.txt". (portuguese)
"""

src_folder = "transcriptor_src/"
dest_folder = "transcriptor_dest/"
audio_paths = listdir(src_folder)

r = sr.Recognizer()
for audio_path in audio_paths:
    with sr.AudioFile(src_folder+audio_path) as source:
        audio = r.record(source)

        try: transcp = r.recognize_google(audio, language="pt-BR")
        except sr.UnknownValueError: transcp = 'failed to convert.\n'

        with open(f"{dest_folder}{audio_path[:-4]}.txt",'w', encoding="utf-8") as fl: fl.write(transcp+'\n')

