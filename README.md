# Welcome to my chess bot / chess engine
I made this mostly just for fun and a bit of experience, using some stuff I learned in my AI class. I currently have a random bot which makes random choices and a minimax bot using alpha beta pruning. The minimax bot is still quite slow, I will optimize it later 


# setup
Setup is pretty simple, make sure you have a mac and conda installed, then just run
```
conda env create -f chessEnv.yaml
```
and then
```
conda activate chessEnv
```

Might add linux support later

# How to play
To play, first make sure you are in the correct conda environment. If you are not, run
```
conda activate chessEnv
```
Once you've done that, just run
```
python playChess.py
```
and you should be set!

