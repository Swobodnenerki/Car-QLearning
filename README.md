# Car-QLearning

# Alex

## How to install packages
In this folder activate venv, pip in venv. 

## How to instantiate VENV 
C:\Users\Alex\AppData\Local\Programs\Python\Python39\python.exe -m venv venv

## Powershell Policy Adaptation (start PS as Admin)
Set-ExecutionPolicy -ExecutionPolicy Unrestricted

## Update pip
C:\Users\Alex\Documents\GitHub\Car-QLearning\venv\bin\python.exe -m pip install --upgrade pip

## Requires Python 3.9 because of PyGame, that doesn't support 3.10 yet (14/05/22)

## Strategies

# 1: Plug in different DDQN algorithm.
Understand environment defined by CB (reward, punishment, episode, session cycle) and adapt. Now it's kind of a mess, study specification of a "good" environment and shape according to it.

# 2: Make it work
main.py at this points calculates something but doesn't render. QLearningFromMate.py renders but doesn't calculate. Combine both to get a working thing. Potentially difficult because Game, AI and Render Logic is nested. 

IDEA Regarding 2: Make MyWindowClass in QLearningFromOldMate and see whether it still renders. If yes, then render issue from main.py might be easily resolvable.