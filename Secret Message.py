import os
from string import digits

def rename_files():

    #go to the folder the files are in
    file_list = os.listdir(r"C:\Users\kamga\Downloads\prank\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Users\kamga\Downloads\prank\prank")
    print("current working directory is " + os.getcwd())
    #click on each file's name and rewrite it
    remove_digits = str.maketrans('', '', digits)
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(remove_digits))
        os.rename(file_name, file_name.translate(remove_digits))
    os.chdir(saved_path)


rename_files()
