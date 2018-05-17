def get_all_files(path_string):
    all_files = []
    p = Path(path_string)

    for file_or_folder in p.iterdir():
        if file_or_folder.is_dir():
            print(str(file_or_folder) + " is a folder")
            f = Path(path_string + '/' + str(file_or_folder) + '/')
            print("reading " + str(f))
            get_all_files(f)
        else:
            all_files.append(file_or_folder)
    return all_files