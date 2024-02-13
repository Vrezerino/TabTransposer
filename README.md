# TabTransposer
## This utility returns a copy of your guitar tabulature file but with transposed notes (fretboard fret numbers).

It is actually not straightforward to transpose tabs at all, and it was my core challenge to make an algorithm that works:
If a two-digit number becomes a one-digit number (e.g. 12 to 9), the program has to pad it with a symbol that denotes a pause,
after detecting what the symbol is in the first place (a space or a hyphen for instance), and also decide what to do if we're
at the end of a line.

## 1. Choose file.
## 2. Input the amount of semitones you want to transpose your tabs with.
## 3. Enjoy your new tabs!

```
|'''|'''|'''|'''
7---12--9-5--9^-
--9-------------
```

After transposing a minor third down (3 semitones):

```
|'''|'''|'''|'''
4---9---6-2--6^-
--6-------------
```

It works with any symbols between the fret numbers.

```
|'''|'''|'''|'''
7   12  9 5  9^ 
  9            
```

Becomes:

```
|'''|'''|'''|'''
4   9   6 2  6^ 
  6          
```
