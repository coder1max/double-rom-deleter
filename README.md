# **Double ROM deleter**

_Disclaimer : I am not responsible for you downloading any ROMs, this is just a tool._

With _Double ROM deleter_, you can delete files from ROMSets which aren't in your language but also exist in your language.
For example, imagine we download and extract a ROMSet with three games :
- _Folder_
  - `game1 (Europe).zip`
  - `game1 (USA).zip`
  - `game2 (USA).zip`

Pretty cool, huh? But one thing annoys us here : we don't need two versions of a game...
Why would we download both the Europe and USA versions of the first game? All I want is just the Europe version. That is why I made this little Python program, which will delete, as I said before, every ROM which I already have in my language.

In this case, once you indicated the right path to the folder containing the ROMs, the program will search for the extensions that contain the languages you don't want, and create a new name which could be the one of the language you choose :
````
if '(USA)' in filename or '(Japan)' in filename or '(World)' in filename:
  name = extract_without_region(filename)
  europe = name + ' (Europe).' + extension 
````

Then, it's going to check if there is really a version in the language you want by searching the name with the selected language that it created in the last line of the previous code. If it exists, the file(s) in another language is/are deleted. If not, it stays here, since there isn't a version in your language : 
```
if os.path.exists(os.path.join(folder_path, europe)):
  os.remove(os.path.join(folder_path, filename))
  print('File deleted : ' + filename)
```

And that's it! I hope this program will be useful to some people, don't hesitate to give me suggestions!