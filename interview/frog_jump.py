def cross_river(path, idx=0, speed=0): #boolean
    #parse the path
    if speed < 0:
        return False
    if len(path) <= idx:
        return True
    element = path[idx]
    if element == "*":
        if speed == 0:
            return cross_river(path, idx+2, speed+1)
        else:
            return cross_river(path, idx+2, speed-1) or cross_river(path, idx+2, speed) or cross_river(path, idx+2, speed+1)
    elif element == "~":
        return cross_river(path, idx+2, speed -1)


assert cross_river('',0) == True
assert cross_river('~',0) == False
assert cross_river('*',0,0) == True
assert cross_river('* ~',0,0) == True
assert cross_river('~ ~',0,0) == False
assert cross_river('* * ~ * ~ ~ *', 0, 0) == True
# frog
# * * ~ * ~ ~ *
# rock *
# water ~
# speech 2 --> 1, 2, 3
# initial speed 0
# * * ~ * ~ ~ *
'''
  (0,1) 
    1-(-1,0,1)
    0,1, 2 => false  #(path remaining, speed) 
    if speed < 0:
        return false
    speed should be atleast one to cross over the ~
    speed is reduced by one crossing over the river (speed-1)
    1(1)2(-1,0,1)
'''
# * * ~ * ~ ~ *
# 0 1   2     3

''' 
#test conditions
# ~ * ~ ~ * - false
# ~ ~ - * - false
'''
