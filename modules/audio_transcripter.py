import speech_recognition as sr
from os import listdir, getcwd, path
from choose_folder import choose_folder_from_path

def transcript_audios_in_folder(folder_path: str=getcwd()) -> list[str]:
    """
    Transcripts all the .wav's in the folder.\n
    Returns a list with all the converted audios paths.\n
    """
    transc_audios = []

    audio_paths = listdir(folder_path)

    r = sr.Recognizer()
    for audio_path in audio_paths:
        file_name, extesion = path.splitext(audio_path)

        if extesion != '.wav': continue
        
        with sr.AudioFile(path.join(folder_path,audio_path)) as source:
            audio = r.record(source)

            try: transcp = r.recognize_google(audio, language="pt-BR")
            except sr.UnknownValueError: transcp = 'failed to convert.\n'

            with open(path.join(folder_path, file_name+".txt"),'w', encoding="utf-8") as fl: fl.write(transcp+'\n')

            transc_audios.append(path.join(folder_path,audio_path))

    return transc_audios

if __name__ == "__main__":
    transcript_audios_in_folder(choose_folder_from_path())