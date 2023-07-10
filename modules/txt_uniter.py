from os import listdir, path, getcwd
if __name__ != "__main__": from modules.choose_folder import choose_folder_from_path
else: from choose_folder import *

def unite_txts_in_folder(folder_path: str=getcwd()) -> list[str]:
    """
    Unites all the .txt's in a folder into one single .txt.\n
    Default folder and destiny folder are the current folder.\n
    Returns a list with all the united .txt's.\n
    """
    united_txts = []

    txt_files = listdir(folder_path)

    with open(path.join(folder_path,"transcript.txt"), "w", encoding="utf-8") as union:
        for txt_file in txt_files:
            file_name, extension = path.splitext(txt_file)

            if extension != ".txt": continue

            with open(path.join(folder_path,txt_file), "r", encoding='utf-8') as part:
                union.write(part.read() + '\n')
            
            united_txts.append(path.join(folder_path,txt_file))

    return united_txts
            
if __name__ == "__main__":
    unite_txts_in_folder(choose_folder_from_path())