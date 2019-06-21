# x=[0,6,8,0,0,1,2,0,0,0,3,7,8,0,0,3,5,0,6,0,0,0]
# x=[1,2,3,4,0,0,5,6,7,8]
x=[1, 2, 3, 4, 5, 0, 0, 6, 7, 8, 8]
zero = -1
non_zero_counter = 0

# print "input: ",
for j in xrange(0,len(x)):
    pass
    # print x[j],

# print

for i in xrange(0, len(x)):
    if x[i] == 0:
        # Find the position of first 0, and set
        # position if it hasn't already been set
        if zero == -1:
            print i, x[i]
            zero = i
        continue
    else:
        # Increase number of non-zero ints
        non_zero_counter += 1

        # Swap zero for non-zero if we
        # know the zero's position
        if zero != -1:
            print zero
            x[zero] = x[i]
            x[i] = 0
            zero += 1
        else:
            continue
    # print x

print x
print "Total number of non-zero ints are: " + str(non_zero_counter)