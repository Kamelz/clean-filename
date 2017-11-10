import os

# -------------------- App functions------------------

# return the path of the files.


def get_files_path(files_path):
    return os.getcwd() + "/" + files_path + "/"


# remove numbers from a file name

def rename(filename, path):
    translation_table = str.maketrans("0123456789", "          ", "0123456789")
    new_name = filename.translate(translation_table)
    os.rename(path + filename, path + new_name)
    return new_name

# clean the files in [files] directory.


def clean(files_path):
    path = get_files_path(files_path)

    for filename in os.listdir(path):
        new_name = rename(filename, path)
        print(filename + " renamed to " + new_name)

# -------------------- Main app ------------------


clean("files")
