#!/usr/bin/env python3

from matplotlib import pyplot as plt
import numpy as np

def tshow(ts):
    #plt.subplot(-3, -3, 1)
    #ords = np.arange(-3, -3, 0.1)
    x = np.linspace(-3, 3, 3300)
    #y = np.array(range(len(ts)))
    #plt.plot(x, ts)
    plt.plot(ts) 
    plt.show()

def main():
    with open("8vers10.txt", "r") as f:
        ts = f.read().split("\n")
        r = [float(x) for x in ts if x != ""]
        #ts.remove(ts[-1])
        tshow(np.array(r))

main()
