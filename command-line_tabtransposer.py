from functools import reduce
import tkinter as tk
from tkinter import filedialog, messagebox as mb

root = tk.Tk()
root.withdraw()

def transpose():
    try:
        originalFilepath = filedialog.askopenfilename()
        nameAndExtension = originalFilepath.split('.')
        #Append "_copy" to new file's name and attach extension.
        copyFilepath = nameAndExtension[0] + "_copy." + nameAndExtension[1]

        semitones = int(input('Transpose up or down, and by how many semitones? E.g -2 or 4: '))
        originalFile = open(originalFilepath)
        copyFile = open(copyFilepath, 'w')

        for line in originalFile:
            # Create a list of every character in the line for iteration and manipulation, and an empty list.
            chars = [*line]
            newChars = []

            i = 0
            while i < len(chars) - 1:
                x = chars[i]
                y = chars[i + 1]
                rest = ''

                #Attempting to detect and capture the symbol denoting rest or pause between notes.
                if x.isdigit() and not y.isdigit() and y != '\t' and y != '\n':
                    rest = x

                #If the fret number is two-digit, concatenate the digits back into a number and transpose it.
                if x.isdigit() and y.isdigit():
                    z = int(x + y) + semitones
                    #Skip the characters because both of them were compared already.
                    i += 1
                    newChars.append(str(z))
                    #If after transposing the number is now a one-digit number, append the pause/rest symbol.
                    if len(str(z)) == 1:
                        newChars.append(rest)
                elif i == len(chars) - 2:
                    z = y
                    if z.isdigit():
                        z = int(z) + semitones
                    newChars.append(x)
                    newChars.append(str(z))
                elif i == len(chars) - 1 and y == '\n':
                    newChars.append(y)
                else:
                    z = x
                    if z.isdigit():
                        z = int(z) + semitones
                    newChars.append(str(z))
                i += 1

            #Write new line into file, as a string.
            newLine = ''.join(newChars)
            copyFile.write(newLine)
            print(newLine)
    except IOError:
        print('IOError')
transpose()