
# Print the numbers described in the exercise
# range function produces a range of values (first, last, steps)
# without end it prints a new line. 
# last print is used to create a new line
a = 10
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

    