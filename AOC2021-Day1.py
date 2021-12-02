#AOC 2021 Day 1: Sonar Sweep
from collections import deque

def mainA():
    #How many measurements are larger than the previous?
    with open('AOC2021-Day1.ini', 'r') as f:
        puzzle = [int(i.rstrip()) for i in f.readlines()]

    inc = [f"{i}:{p} inc" for i,p in enumerate(puzzle[1:],1) if (p-puzzle[i-1])>0]
    print(f'Number of meas larger than prev: {len(inc)}')
    #Answer: 1681

def mainB():
    #Using a three-measurement sliding window, how many windows are larger than previous?
    with open('AOC2021-Day1.ini', 'r') as f:
        puzzle = [int(i.rstrip()) for i in f.readlines()]
    window = deque([],3)
    windows = []
    for p in puzzle[:-2]: #Moving window will move beyond last 2 elements
        window.append(p)
        windows.append(sum(window))
    inc = [f"{i}:{w} inc" for i,w in enumerate(windows[1:],1) if (w-windows[i-1])>0]
    print(f'Number of meas larger than prev: {len(inc)}')
    #Answer: 1702

if __name__ == "__main__":
    mainA()
    mainB()

