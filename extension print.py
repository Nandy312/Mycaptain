Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filename = input("filename.py: ")
filename.py: py
>>> file_ext = filename.split(".")
>>> print("The extension of the file is:" + repr(file_ext[-1]))
The extension of the file is:'py'
>>> 