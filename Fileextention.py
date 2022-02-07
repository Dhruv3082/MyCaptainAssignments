# Here we are going to write a code which shows us the extention of file 

filename = input('Input the file name :') # File name is abc.py

file_ext = filename.split(".") # Splits the string after "."

print(" The extension of the file is :" +repr(file_ext[-1])) # The output is 'py'