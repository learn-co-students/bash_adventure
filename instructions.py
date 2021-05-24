
from IPython.display import Markdown, display
import os


def instructions():
    
    cwd = os.getcwd()
    path = os.path.join(cwd)
    text = f"""# Bash Adventure\n\n**This activity focuses on Bash Fundamentals. The following skills will be used:**
- Running a provided bash command.
- Running a .py file.
- Printing the contents of a directory.
- Creating a new directory.
- Navigating a directory.
- Making an edit to a text file using `vim`.
- Moving a file.\n\n
**If you are running this lab in Illumidesk, at the end of these instructions, we provide a link that will take you to a terminal window. If you are running the lab locally, you will complete the lab in your local terminal window.**\n\n
## Once you have a terminal window open, please complete the following tasks:
\n\n>*Automated tests have been provided at the end of this notebook to check your work. For this lab, the tests will be checking to see if folders and files have been placed in the correct location. Be sure to carefully follow the instructions below!*\n\n### Task 1
1. run the command `cd {path}` (Please notify an instructor if this command does not work)
2. run the following setup up commands (Don't worry too much about this step, these are just needed because we're running the lab in illumidesk)
    - pip install pyvim
    - alias vim=pyvim
3. Use the `ls` command to print the contents of the directory.
4. run the .py file called `begin_mission.py` by running the command `python begin_mission.py`
5. Find the README.md file.
6. Add the phrase "Fear not the terminal." to the readme file.

### Task 2
Once you have made an edit to the README.md file:
1. Create a new folder called "buried_treasure_chest".
2. Move the README.md file into that folder.\n\n## Begin the adventure\n\nIf you are running this lab on your local computer, open a terminal window, and begin task 1.
\n\n<a href="/user/x/terminals/1" target="_blank"><b>If you are funning this lab on Illumidesk, click here to begin!</b></a>
> **NOTE:** We have had issues with this functionality in Illumidesk. If the screen that appears does not have a black square, please notify and instructor. We will have to open a terminal window in your jupyter file system and then begin with the first task. If the terminal page opens, use your mouse to click into the terminal window, and then hit the enter key.
> - (This is not typically a requirement for running commands in terminal, but is necessary when running this lab on an Illumidesk server!)
    
    """
    
    display(Markdown(text))