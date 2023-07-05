from os import listdir

"""
This program unites all .txt in a folder into a slide .txt file.
"""

src_folder = "uniter_src/"
dest_file = "union.txt"

txt_files = listdir(src_folder)

# ordenate files.
def cut_of(string: str) -> int:
    string = string.removeprefix("ent_audio_ARH_")
    string = string.removesuffix(".txt")
    return int(string)

txt_files.sort(key=lambda x: cut_of(x))
# ----------------- #

with open(dest_file, "w", encoding='utf-8') as union:
    for txt_file in txt_files:
        with open(src_folder+txt_file, "r", encoding='utf-8') as part:
            union.write( part.read() + '\n' )