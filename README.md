# Welcome to the Hunt The Wumpus

<p align="center">
  <img src="https://github.com/pedrolemoz/huntthewumpus/blob/master/assets/logo.png" alt="Hunt the Wumpus"/>

## This game  is the final project of a programming subject in Computer Science course.

* Written in Python3 with PyGame library. In Portuguese.

> Created by Pedro Lemos & Klaus Pereira.
> Original game by Gregory Yob.

### Getting started

In order to play this game (and see how it's running), you'll need:

* Latest version of Python3
* Latest version of PyGame library

### How to install

#### In GNU/Linux

  If you are using GNU/Linux, you probably already have Python3 installed in your system by default.
  
  To install PyGame in Ubuntu-based distros in version 19.04 and later:
  
  ```
  sudo apt install python3-pygame
  ```

  To install PyGame in Ubuntu-based distros in version 16.04 or older:

  ```
  sudo apt install python3-setuptools && sudo easy_install3 pip && sudo pip3.5 install pygame
  ```

#### Running

  Open your terminal. You can use the ```Ctrl + Alt + T``` shortcut.
  Look up for the directory that you have unzipped the game file using ```cd``` command. Try ```pwd``` if you have no idea of where you are.
  Once you are in the game folder, type:

  ```
  python3 main_game_desktop.py
  ```
  > Note: There are two versions avaliable: desktop and mobile

  To close the game, just close the actual window of the game, or the terminal.
  To force the stop, press ```Ctrl + C```.

#### In Windows

  To install Python3, please visit [Python official website](https://www.python.org/downloads/), download and install the latest package available.

  To install PyGame, with Python3 already installed, open the command prompt and type the following:

  ```
  py -m pip install -U pygame --user
  ```

  ```
  py -m pip install --upgrade pip
  ```

#### Running

  Once you have everything installed, just double click the ```main_code_desktop.py``` file to open the game.
  You can also open the file with IDLE and run it with ```F5``` button.
  And of course, you can use the command prompt to open the game file.
  In this case, you may have to add your Python3 path to the environment variables in order to do it.

#### In Android (new)

  Recently I found a way to run this game in Android. I attempted to use [QPython3](https://play.google.com/store/apps/details?id=org.qpython.qpy3), but unfortunately it was not possible.
  Then I tried [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3) and it worked fine!
  
  In order to run this game in Android, download the latest released package.
  Then, download [PyDroid 3](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3).
  Open ```main_code_mobile.py``` and click run. You're done.

  Notes: this version can be unstable and buggy, because of PyGame's implementation in PyDroid. Isn't the real PyGame there.
  You can try another application to run this game (such QPython3), by installing ```pygame-sdl2``` package via ```pip3```. Not guaranteed.

### The game itself


#### Objective

  You are in the world of Wumpus. This world is dangerous.
  There are pits that you could fall into, and obviously, the monster.
  Your main objective is collect one gold coin, that can be anywhere in the world, and return to the begin of the world.
  You have one bow and an arrow, which can be used to defeat the terrible Wumpus.

#### Gameplay

  You can win this game in two ways:

  - Collecting the gold and returning to the begining of the game.
  - Collecting the gold, defeating the Wumpus with one shot and returning to the begining of the game.

  You die if:
  
  - You fall into a pit.
  - You enter the same place Wumpus is.

  Easy enough, huh?

  It might not be easy as you expect.

  Everytime you perform a movement, you lose one point (even if you has zero points).
  You only get a score if, and only if, you collect the gold coin or defeat Wumpus. Otherwise, you ain't get nothing.
  You have just one arrow. Use it wisely.

  #### Scoring

  - If you die by any reason, you'll lose 10.000 points.
  - If you defeat Wumpus, you'll get 10.000 points.
  - If you collect the gold coin, you'll get 1.000 points.
  - If you return to the begining of the game after collecting coin, you'll get 100 extra points.

  #### Controls

  ```W, A, S, D``` or ```←, ↑, ↓, →``` to move the character.
  
  ```F``` to shoot your arrow.
  
  ```P``` to pause the game.
  
  ```ESC``` to exit the scores menu.

#### How was it made?

  The game screen is a huge matrix. We have x and y axis to work on.
  We use object-oriented programming in Python to organize things together.
  A lot of variables, lists and ```if``` statements are being used to perform verifications and get the game actually working.
  Keep in mind that a game is a infinite loop, which is updated 60 times per second. Everything is [blited](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit). Everytime.

### Bugs

  Nothing is perfect. Our project isn't too. There are some bugs in this game:

  - When you shoot the arrow, player doesn't change it's image instantly (without arrow). You need to walk to update.
  - When you win, sometimes you don't return to main menu.
