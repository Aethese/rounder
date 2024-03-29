# Rounder [![Tests](https://github.com/Aethese/rounder/actions/workflows/run_test.yml/badge.svg?branch=main)](https://github.com/Aethese/rounder/actions/workflows/run_test.yml) [![DeepSource](https://deepsource.io/gh/Aethese/rounder.svg/?label=active+issues&show_trend=true&token=OPtRN7JhnzQXx7u2RUI-dz45)](https://deepsource.io/gh/Aethese/rounder/?ref=repository-badge)
Rounder is a ***fast***, lightweight implementation of the built-in round function in Python. It allows for **advanced** rounding with the use of **artificial intelligence** to round fully and completely. It rounds even better than the built-in round function with it's rounding accuracy. It's made to be as customizable as possible with options such as how many digits you want rounded (even though that's a granted feature), change return format on error, and the option to disable warnings.

# How it works and how to use
**Python 3.8 and above supported!** You can use it just like the built-in round function, with option for round to digit place (for example: the hundredths place) and it will round the float you passed to the digit place you specified. If you didn't specify a round place it will automatically round by the whole number. The return value for whole numbers will always be `int`, while floats will obviously be a `float`.

## Example uses
```py
>>> import rounder
>>> rounder.round(3.14159)
Output: 3
Type: int
>>> rounder.round(3.14159, 1)
Output: 3.1
Type: float
```

## Installation
Installation is as simple as moving the `rounder` folder to your working directory. There is no PIP installation at this time.

# Is this production ready?
Probably not. There are many use cases that just haven't been tested yet. I do use Rounder a lot for some of my personal projects because it has been stable for my use cases.

# Why use Rounder
## Comparing to built-in round function
Rounder, compared to the built-in round function of Python, is more 'advanced' and fast. What I mean is that it rounds beyonds the digit place you want for a more exact round with the help of **artificial intelligence**. For example: `3.44445` rounded to the tenth place should be `3.5` if you round all the way through, which Rounder identifies correctly. Although it should be `3.5` (if you round all the way), the built-in round function defines it as `3.4`. You may have different views on how to round, such as not rounding all the way through, so of course you can always use the built-in round function.

## Speed
Rounder, overall, is faster than the built-in round function. You can check this info yourself by taking a look at the latest build tests.

# Why Rounder was made
I just wanted a fun challenge, and recreating a more advanced version of the built-in round function without using any modules sounded like a hard and perfect challenge for me :)
