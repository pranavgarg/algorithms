def towers_of_hanoi(n, from_peg, end_peg, temp_peg):
    if n == 0:
        return
    towers_of_hanoi(n-1, from_peg, temp_peg, end_peg)
    print "move disk {} from {} -> {}".format(n, from_peg, end_peg)
    towers_of_hanoi(n-1, temp_peg, end_peg, from_peg)

towers_of_hanoi(3, "start","end","temp")