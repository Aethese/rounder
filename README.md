# Rounder
My fast custom implementation of the built in 'round' function. This was for class, please don't judge *at least I had fun making it*. I have no clue how it works, but it works (to my knowledge). Feel free to look at the source code and the tests I use to test it :)

# How it works and how to use
You will pass a float with a round to digit place (for example: hundredths) and it will round that float to that digit place. You don't have to pass round to digit place if you want to just round by the whole number (will return an integer). Example uses below:
```py
rounder.round(3.14159)
# Output: 3
rounder.round(3.14159, 1)
# Output: 3.1
```

# Fun fact
Rounder seems to be faster than the built in round function (you can see my speed tests in `tests.py`)! Take that Python!

# Why?
Well first off, I kind of had to make this for a grade. Also I just wanted to make my own custom implemented round function for a while now (don't ask why), so this was the perfect excuse to make it. Feel free to actually use and edit the project to work to your liking. If you want to improve it feel free to make a pull request :)
