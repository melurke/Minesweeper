# Minesweeper

Bot that plays Minesweeper on https://minesweeperonline.com/
The game should be played with the compiler in the right half of the screen and the website on the left half.

The record for expert mode is 20 seconds, which is 19 seconds faster than the record before. At the moment you can still see this on the website, but I suspect that I will get banned in the future as this happened before.

<img src="record.png">

expert.py / intermediate.py / beginner.py -> Main programs that play the game in the different difficulty levels of the site

functions.py -> Function definitions for the main program

cool_bot.py -> Bot for the beginner mode of the website trying to win with the first click

PIL_vs_PyAutoGUI.py -> Test to see if PIL can scan the field faster than PyAutoGUI (it can)
