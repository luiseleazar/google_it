import os

#2.xxxxx directory
DIR = '2.interact_with_os/handle_files'
for name in os.listdir("."):
    fullname = os.path.join(DIR, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")
