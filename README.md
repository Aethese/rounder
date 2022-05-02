# Rounder
My ***fast*** custom implementation of the built in `round` function in Python. I have no clue how it works, but it works (to my knowledge). Feel free to look at the source code and the tests I use to test it :)

# How it works and how to use
**Python 3.8 and above supported!** You will pass a float with a 'round to' digit place (for example: hundredths), and it will round that float to that digit place you specified. If you want to round by the whole number, you can either pass a 0 for round place or don't pass any round places. The return value will be `int`. Example uses below:
```py
rounder.round(3.14159)
>>> Output: 3
>>> Type: int
rounder.round(3.14159, 1)
>>> Output: 3.1
>>> Type: float
```
## Please note
If you do attempt to round something that isn't a float or your round place is bigger than the current available digits, Rounder will just return your original passed number. You can change that by editing the `rounder.return_format` variable through code or just hard coding the change with the documentation above the variable (only 3 options). Of course, feel free to add your own

# Why use Rounder
## Comparing to built-in round function
Rounder, compared to the built-in round function of Python, is more 'advanced'. What I mean is that it rounds beyonds the number you want for a more estimate round. For example: 3.44445 rounded to the tenth place should be 3.5 if you round all the way through, which Rounder identifies correctly. Although it should be 3.5 (if you round all the way), the built-in round function defines it as 3.4. You may have different views on how to round so of course you can always use the built-in round function. 

## Speed
Rounder, overall, is faster than the built-in round function. You can check this info yourself by taking a look at the latest build tests.
