#AOC 2021 Day 2: Dive!
from collections import deque

def mainA():
    #Find Horiz position & depth  (Final answer: multiply pos + depth)
    with open('AOC2021-Day2.ini', 'r') as f:
        puzzle = [i.rstrip().split(' ') for i in f.readlines()]
        commands = [(c,int(q)) for c,q in puzzle]

    x,d = 0,0
    for comm,q in commands:
        if comm == 'forward':
            x += q
        elif comm == 'down':
            d += q
        elif comm == 'up':
            d -= q
        else:
            raise ValueError(f'{comm} not recognized')

    print(f'Horiz position: {x}')
    print(f'Depth: {d}')
    print(f'Answer: {x*d}')
    #Answer: 2150351

def mainB():
    #Adds 'aim' component  (Final answer: multiply pos + depth)
    with open('AOC2021-Day2.ini', 'r') as f:
        puzzle = [i.rstrip().split(' ') for i in f.readlines()]
        commands = [(c,int(q)) for c,q in puzzle]

    x,d,a = 0,0,0
    for comm,q in commands:
        if comm == 'forward':
            x += q
            d += a*q
        elif comm == 'down':
            a += q
        elif comm == 'up':
            a -= q
        else:
            raise ValueError(f'{comm} not recognized')

    print(f'Horiz position: {x}')
    print(f'Depth: {d}')
    print(f'Aim: {a}')
    print(f'Answer: {x*d}')
    #Answer: 1842742223

if __name__ == "__main__":
    #mainA()
    mainB()

