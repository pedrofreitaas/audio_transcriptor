"""
This program converts video into text.
Works only for portuguese. (Pt-BR)
"""

from os import remove, mkdir
import video_converter as vd_conv
import audio_converter as ad_conv
import audio_divisor as ad_div
import audio_transcripter as ad_transc
import uniter

def remove_files(list_of_paths: list[str]) -> None:
    for file in list_of_paths:
        try: remove(file)
        except: pass

if __name__ == "__main__":
    src_folder = "source/"
    
    try: mkdir(src_folder)
    except: pass

    remove_files([src_folder+"transcript.txt"])

    # convert the video to audio.
    vd_conv.convert_videos_in_folder(src_folder)

    # convert the audio to a supported file extension.
    conv_audios = ad_conv.convert_audios_in_folder(src_folder)
    remove_files(conv_audios)

    # divide the audio cause it can be longer than supported
    divided_audios = ad_div.divide_audios_in_folder(src_folder, 30)
    remove_files(divided_audios)

    # transcript each part.
    transc_audios = ad_transc.transcript_audios_in_folder(src_folder)
    remove_files(transc_audios)

    # unite every part.
    united_txts = uniter.unite_txts_in_folder(src_folder)
    remove_files(united_txts)