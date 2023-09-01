import time
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

root = tk.Tk()
root.withdraw()

def transpose():
    try:
        originalFilepath = filedialog.askopenfilename()
        nameAndExtension = originalFilepath.split('.')
        #Append "_transposed" to new file's name and attach extension.
        transposedFilepath = nameAndExtension[0] + "_transposed." + nameAndExtension[1]

        semitones = int(simpledialog.askinteger('TabTransposer', 'Transpose up or down, and by how many semitones? For example, -2 or 4: '))
        originalFile = open(originalFilepath)
        copyFile = open(transposedFilepath, 'w')

        #Start timer for elapsed time info in the final messagebox.
        startTime = time.time()
        #Function to attempt to detect the symbol in between fret numbers.
        def mostCommonChar(list):
            return max(set(list), key = list.count)

        for line in originalFile:
            # Create a list of every character in the line for iteration and manipulation, and an empty list.
            chars = [*line]
            newChars = []
            rest = mostCommonChar(chars)

            i = 0
            while i < len(chars) - 1:
                x = chars[i]
                if len(chars) == 1:
                    newChars.append(x)
                y = chars[i + 1]

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
                #elif x == '\n' or (i == len(chars) - 1 and y == '\n'):
                #    newChars.append(y)
                else:
                    z = x
                    if z.isdigit():
                        z = int(z) + semitones
                    newChars.append(str(z))
                i += 1

            #Write new line into file, as a string.
            newLine = ''.join(newChars)

            if newLine == '':
                copyFile.write('\n')
            else:
                copyFile.write(newLine)

        endTime = time.time()
        elapsedTime = str(endTime - startTime)[:6]
        messagebox.showinfo('Done', 'Transposition finished in ' + elapsedTime + ' seconds!')
    except IOError:
        print('IOError')
transpose()
