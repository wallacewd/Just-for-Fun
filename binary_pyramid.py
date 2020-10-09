"""
Pyramid Generator
Dan Wallace
10/07/20
www.brick.technology
"""

import time

# User Control Variables
max_height = 25                             # How high do you want your pyramids?
num_pyramid = 5                             # How many pyramids do you want?

# Loop Controls
time_thru = 1
max_height_mem = max_height
pyramid_thru = 1

# Main loop container 
while pyramid_thru <= num_pyramid:

    # Pyramid Up
    for a in range(max_height):
        if time_thru < max_height:
            for b in range(a):
                if (time_thru%2) == 0:
                    print("0",end="")
                else:
                    print("1", end="")
            print("\\",end="")                 
            print("",end="\n")
            time.sleep(0.001)
            time_thru +=1

    # Pyramid Down
    down_start = 1
    for c in range(max_height-1):
        if time_thru-1 >= 0:
            for d in range(max_height-1):
                if (time_thru%2) == 0:
                    print("0",end="")
                else:
                    print("1", end="")
            if down_start == 1:
                print("}",end="")
                down_start = 0
            else:
                print("/",end="")
            print("",end="\n")
            time.sleep(0.001)
            time_thru -=1
            max_height -=1
    max_height = max_height_mem
    pyramid_thru += 1
    if max_height == max_height_mem:
        print("/")
    else:
        pass     
