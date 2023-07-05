import speech_recognition as sr
from os import listdir

def transcript_audios_in_folder(folder_path: str) -> list[str]:
    """
    Transcripts all the .wav's in the folder.\n
    Returns a list with all the converted audios paths.\n
    """
    transc_audios = []

    audio_paths = listdir(folder_path)

    r = sr.Recognizer()
    for audio_path in audio_paths:
        if audio_path[-4:] != '.wav': continue
        
        with sr.AudioFile(folder_path+audio_path) as source:
            audio = r.record(source)

            try: transcp = r.recognize_google(audio, language="pt-BR")
            except sr.UnknownValueError: transcp = 'failed to convert.\n'

            with open(f"{folder_path}{audio_path[:-4]}.txt",'w', encoding="utf-8") as fl: fl.write(transcp+'\n')

            transc_audios.append(folder_path+audio_path)

    return transc_audios
