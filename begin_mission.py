import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
print()
print('===============================================')
print(color.BOLD + 'Hi There!' + color.END)
print()
print(color.UNDERLINE + 'You have received the following mission' + color.END)
print()
print()
print(color.BLUE + 'I have created three doors...')
print('Somewhere, behind one of these doors, there is a README.md file.')
print('...')
print('But it seems to be hidden...')
print()
print(color.RED + 'I have left you some clues for finding it...' + color.END)
print()
print(color.BOLD + 'Please find the README.md file and add your name to the file.')
print('Once you have edited the file, move it to the room (folder) we\'re in now, and push it to github!')
print()
print(color.BOLD + 'Happy searching :)' + color.END)
print('===============================================')
print()

def write_clue(clue_path, message):
    with open(clue_path, 'w') as clue:
        clue.write(message)

os.mkdir('door_1')
os.mkdir('door_2')
os.mkdir('door_3')

left = os.path.join('door_1', 'left')
right = os.path.join('door_1', 'right')
os.mkdir(left)
os.mkdir(right)

attic = os.path.join('door_2', 'attic')
basement = os.path.join('door_3', 'basement')
os.mkdir(attic)
os.mkdir(basement)

secret_script = os.path.join(basement, '.secret_fancy_password.py')
with open(secret_script, 'w') as file:
    file.write('file = open("README.md", "w")\n\nfile.write("**My name is:**")\n\nfile.close()')

trick_script = os.path.join(attic, 'mission_complete.sh')
with open(trick_script, 'w') as file:
    file.write('#!/bin/bash\n\nmkdir trapdoor\n\necho "To find the README.md file, you must go to the basement and run python .secret_fancy_password.py" >> final_clue.txt\n\ncd trapdoor\n\n mkdir behind_a_large_plant\n\ncd behind_a_large_plant\n\nmkdir a_shadowy_place\n\ncd a_shadowy_place\n\n echo "lol you fell for a trap! Please return the to the attic for the actual clue!" >> clue_4.txt')

clue_path = os.path.join(left, 'clue_1.txt')
write_clue(clue_path, 'You will need to find the stairs...')

clue_path = os.path.join(right, 'clue_2.txt')
write_clue(clue_path, 'Check the other door!')

clue_path = os.path.join(attic, 'clue_3.txt')
write_clue(clue_path, 'Congrats! Run source mission_complete.sh to collect the README.md file!')

