import os
from tkinter import filedialog

# ENGLISH VERSION

folder_path = filedialog.askdirectory()

language = input("Indicate the language you want to keep (E = Europe / USA / J = Japan / W = World) : ")
extension = input("Indicate the extension type WITHOUT DOT (zip, 7z...) : ")


def extract_without_region(original):
    return original.strip().split('(')[0].strip()


if language == "E":
    for filename in os.listdir(folder_path):
        if '(USA)' in filename or '(Japan)' in filename or '(World)' in filename:
            name = extract_without_region(filename)
            europe = name + ' (Europe).' + extension
            if os.path.exists(os.path.join(folder_path, europe)):
                os.remove(os.path.join(folder_path, filename))
                print('File deleted : ' + filename)

if language == "USA":
    for filename in os.listdir(folder_path):
        if '(Europe)' in filename or '(Japan)' in filename or '(World)' in filename:
            name = extract_without_region(filename)
            usa = name + ' (USA).' + extension
            if os.path.exists(os.path.join(folder_path, usa)):
                os.remove(os.path.join(folder_path, filename))
                print('File deleted : ' + filename)

if language == "J":
    for filename in os.listdir(folder_path):
        if '(USA)' in filename or '(Europe)' in filename or '(World)' in filename:
            name = extract_without_region(filename)
            japan = name + ' (Japan).' + extension
            if os.path.exists(os.path.join(folder_path, japan)):
                os.remove(os.path.join(folder_path, filename))
                print('File deleted : ' + filename)

if language == "W":
    for filename in os.listdir(folder_path):
        if '(USA)' in filename or '(Europe)' in filename or '(Japan)' in filename:
            name = extract_without_region(filename)
            world = name + ' (World).' + extension
            if os.path.exists(os.path.join(folder_path, world)):
                os.remove(os.path.join(folder_path, filename))
                print('File deleted : ' + filename)
