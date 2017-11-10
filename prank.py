import os

# -------------------- App functions------------------

# return the path of the files.

def get_files_path(files_path):
    return os.getcwd() + "/" + files_path + "/"


# remove numbers from files names
def clean(files_path):
    path = get_files_path(files_path)

    for filename in os.listdir(path):
        new_name = ''.join([i for i in filename if not i.isdigit()])
        os.rename(path + filename, path + new_name)
        print(filename + " renamed to " + new_name)

# -------------------- Main app ------------------


clean("files")
