from os import getcwd, scandir, DirEntry

def choose_folder_from_path(path: str=getcwd()) -> str:
    """
    User input based function.\n
    Lists available *folders* in the given path and makes the user choose for one.\n
    Default path is the current folder.\n
    Returns the choosen path.\n
    """
    dirs = list(filter(DirEntry.is_dir, scandir(path)))

    for i, dir in enumerate(dirs):
        print(i+1, dir.path)
    
    while True:
        try:
            choosen_folder = dirs[int(input('Choose a folder: '))-1]
            break
        except: print('Invalid option.')

    return choosen_folder.path