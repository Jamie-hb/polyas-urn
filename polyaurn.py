# simulates drawing balls from Polya's urn. Current code fills the urn with 3 colours, but can easily be adapted to more/less.
# at each iteration, a ball is drawn and replaced along with another ball of the same colour
#idea: get code to plot a graph of how many white, black, ... balls at each iteration?

import random

# inital number of balls
white = 1 
black = 1
red = 1
# number of balls drawn of each colour
W = 0 
B = 0 
R = 0 
N = 500000 # total number of balls to draw

for i in range(N):
    T = white + black + red
    p = white / T  
    q = red / T
    x = random.uniform(0,1)
    if x <= p:
        W = W + 1
        white = white + 1
    elif x <= p + q:
        R = R + 1
        red = red + 1
    else:
        B = B + 1
        black = black + 1

print('Number of white balls = ' + str(W) + '. ' + str(100 * (W / N))+ '%.')
print('Number of black balls = ' + str(B) + '. ' + str(100 * (B / N))+ '%.')
print('Number of red balls = ' + str(R) + '. ' + str(100 * (R / N))+ '%.')
