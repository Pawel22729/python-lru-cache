#!/usr/bin/env python3

import time
from helpers import lru

if __name__ == "__main__":
    # Cache site input
    cacheSize = input("\n### Cache size init: ")
    # LinkedList init
    ll = lru.LinkedList(int(cacheSize))

    # Simple menu
    while isinstance(cacheSize, int):
        key = input("\nCalculate factorial for: ")
        startTime = time.time()        
        ll.getElement(key)
        t = time.time() - startTime
        print('Calculation time: %.6f' % t)
        
        # Printing elements can be uncommented for small numbers, as it will blow up in terminal
        ll.printElements()