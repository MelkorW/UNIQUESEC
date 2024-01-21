from os.path import exists
import os


def writefile(data, file_name):
    if exists(file_name):
        print("File already exists. Do you want to overwrite it? (y/n)")
        overwrite = input()
        if overwrite == "y":
            with open(file_name, 'w') as f:
                f.write(data+"\n")
                print("File overwritten")
        else:
            with open(file_name, 'a') as f:
                f.write(data+"\n")
                print("File appended")
            return
    else:
        print("File does not exist. Do you want to create it? (y/n)")
        create_file = input()
        if create_file == "n":
            return
        else:
            with open(file_name, 'w') as f:
                f.write(data+"\n")
                print("File created")


def list_files_in_directory():
    if os.name == 'nt':
        return(os.system('dir'))
    else:
        return(os.system('ls -la'))
        


def readfile(file_name):
    if exists(file_name):
        with open(file_name, 'r') as f:
            print(f.read())
    else:
        print("File does not exist")


def deletefile(file_name):
    if exists(file_name):
        print("File exists. Do you want to delete it? (y/n)")
        delete = input()
        if delete == "y":
            os.remove(file_name)
            print("File deleted")
        else:
            print("File not deleted")
    else:
        print("File does not exist")


def main():
    print("What do you want to do? (write/read/delete)")
    action = input()
    if action == "write":
        print("Enter the file name: ")
        file_name = input()
        print("Enter the data: ")
        data = input()
        writefile(data, file_name)
    elif action == "read":
        list_files_in_directory()
        print("Enter the file name: ")
        file_name = input()
        readfile(file_name)
    elif action == "delete":
        list_files_in_directory()
        print("Enter the file name: ")
        file_name = input()
        deletefile(file_name)
    else:
        print("Invalid input")


main()