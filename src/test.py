# table= {}
# string = 'larloll'
# i = 0
# for c in string:
#     print(c)
#     if c == 'c' or 'C':
#         i += 1
# print(i)
x ='peterpeter'
dict = {}
for c in x:
    if c not in dict:
        dict[c]=0
    dict[c]+=1
print (dict)
    