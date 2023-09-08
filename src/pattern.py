# Print the pattern
# sep know to only do it between values
for x in range(1,10):
    if x < 6:
        print(*x*('*',), sep=' ')
    
for y in range(4,0,-1):
    print(*y*('*',), sep=' ')



    

