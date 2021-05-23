import os
import glob
from IPython.display import display, Markdown





def generate_paths():
    folder_path = os.path.join('door_3', 'basement', 'buried_treasure_chest')
    file_path = os.path.join(folder_path, 'README.md')
    return folder_path, file_path

def test_folder_path(folder_path):

    if os.path.isdir(folder_path):
        message = Markdown("✅ *The buried_treasure_chest folder was created successfully!*")
    elif glob.glob("./**/*chest", recursive = True):
        message = Markdown("🚫 *The buried_treasure_chest folder was found in the wrong location!*")
    else:
        message = Markdown("🚫 *The buried_treasure_chest folder was not found.*")

    display(message)

def test_file_path(file_path):

    path = file_path
    if os.path.isfile(path):
        message = Markdown("✅ *The README.md file was found in the correct location!*")
    elif glob.glob("./**/README.md", recursive = True):
        message = Markdown("🚫 *The README.md file was found in the wrong location!*")
        path = glob.glob("./**/README.md", recursive = True)[0]
    else:
        message = Markdown("🚫 *The README.md file was not found.*")
        path = None
    
    display(message)
    return path


def test_file_content(file_path):

    file = open(file_path, 'r')
    text = file.read()
    file.close()
    text = text.lower()
    answer = 'fear not the terminal.'.split()
    score = 0
    for word in answer:
        if word in text:
            score += 1
    display(Markdown(f">*{score}/4 of the required words were found in the README.md file.*"))

def test_adventure():
    folder_path, file_path = generate_paths()
    test_folder_path(folder_path)
    path_found = test_file_path(file_path)
    if path_found:
        test_file_content(path_found)
