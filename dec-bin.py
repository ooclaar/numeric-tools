#!/usr/bin/python3.11 env

import sys

if (len(sys.argv) > 1):
    print(sys.argv[1])

    dividendo=sys.argv[1]
    divisor=2
    resto=0
    binario=""

    while( dividendo !=2 and dividendo != 1):
        print(dividendo % divisor)   
