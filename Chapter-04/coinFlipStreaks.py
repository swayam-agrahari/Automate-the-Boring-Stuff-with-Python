# import random
# numberOfStreaks = 0
# my_list=[]
# count = 0
# for experimentNumber in range(10000):
#     # Code that creates a list of 100 'heads' or 'tails' values.
#    for i in range(100):
#       choice = random.randint(0,1)
#       if(i == 0):
#          my_list.append('H')
#       else:
#          my_list.append('T')
   
#    for i, item in enumerate(my_list):
#       if(item == 'H' and count <= 6):
#          count += 1
#       else:
#          count = 0
#          continue
#       if(count == 6):
#          numberOfStreaks += 1
   
#    for i, item in enumerate(my_list):
#       if(item == 'T' and count <= 6):
#          count += 1
#       else:
#          count = 0
#          continue
#       if(count == 6):
#          numberOfStreaks += 1
         
#     # Code that checks if there is a streak of 6 heads or tails in a row.
# print('Chance of streak: %s%%' % (numberOfStreaks / 100))


import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    my_list = []
    for i in range(100):
        choice = random.randint(0, 1)
        if i == 0:
            my_list.append('H')
        else:
            my_list.append('T')

    count = 0
    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i, item in enumerate(my_list):
        if item == 'H' and count < 6:
            count += 1
        else:
            count = 0
            continue
        if count == 6:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % ((numberOfStreaks / 10000) * 100))
