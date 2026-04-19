# text-replace
This script basically does the replace function on .txt files, which replaces all occurences of selected string from file with second selected string.
For example, if you have text file which contains text:
```
i love frogs
```
You can use replace function to replace word "love" for "hate" and now you hate frogs wtf bro **D:**

Script opens a dialog window which gets two strings from user input, first string is original word/sentence which you want to replace in file and second one is the new word,
which will replace all occurences of the selected string in text file.  
Text file selection appears after green button press, it opens a window for user to choose the original .txt file
and then opens a second window to choose path where new file with replaced words will be saved.
Output is saved in new file created by user, or overwrites the old one if selected by user.

To run it on linux you have to download version-specific tkinter package in your package manager, examples for python ver 3.14 which i used:  
  
Arch Linux
```
sudo pacman -S tk
```
Ubuntu/Debian/Mint
```
sudo apt update
sudo apt install python3.14-tk
```
Fedora / RHEL / CentOS
```
sudo dnf install python3.14-tkinter
```
