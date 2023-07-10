from os import remove, mkdir, getcwd, path
import modules.video_converter as vd_conv
import modules.txt_uniter as txt_un
import modules.audio_transcripter as ad_trans
import modules.audio_divisor as ad_div
import modules.audio_converter as ad_conv

def remove_files(list_of_paths: list[str]) -> None:
    """Remove files corresponding to the paths in the parameter.\n"""
    for file in list_of_paths:
        try: remove(file)
        except: pass

if __name__ == "__main__":
    src_folder = "source/"
    
    try: 
        mkdir(src_folder)
        print('Source folder succesfully generated. Put .mp4/.mp3/.wav files inside for transcription.\n')
    except: pass

    remove_files([src_folder+"transcript.txt"])

    # convert the video to audio.
    video_conversions = vd_conv.convert_videos_in_folder(src_folder)

    # convert the audio to a supported file extension.
    audio_conversions = ad_conv.convert_audios_in_folder(src_folder)
    remove_files(video_conversions)

    # divide the audio, because it can be longer than supported.
    division_results = ad_div.divide_audios_in_folder(src_folder, 30)
    remove_files(audio_conversions)

    # transcript each part.
    trans_results = ad_trans.transcript_audios_by_paths(division_results)
    remove_files(division_results)

    # unite every part.
    united_txts = txt_un.unite_txts_in_folder(src_folder)
    remove_files(trans_results)