from os import listdir
from choose_folder import choose_folder_from_path

def unite_txts_in_folder(folder_path: str) -> list[str]:
    """
    Unites all the .txt's in a folder into one single .txt.\n
    Returns a list with all the united .txt's.\n
    """
    united_txts = []

    txt_files = listdir(folder_path)

    with open(folder_path+'transcript.txt', "w", encoding='utf-8') as union:
        for txt_file in txt_files:
            if txt_file[-4:] != '.txt': continue

            with open(folder_path+txt_file, "r", encoding='utf-8') as part:
                union.write( part.read() + '\n' )
            
            united_txts.append(folder_path+txt_file)

    return united_txts
            
if __name__ == "__main__":
    unite_txts_in_folder(choose_folder_from_path())