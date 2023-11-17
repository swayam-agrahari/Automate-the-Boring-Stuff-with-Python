tableData = [['apples', 'oranges', 'cherries', 'banana'],['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]
my_list1=[]
for i in tableData:
   my_list=[]
   for j in i:
      my_list.append(len(j))
   my_list1.append(max(my_list))


for j in range(len(tableData[0])):
   for i in range(len(tableData)):
      
      print(tableData[i][j].rjust(my_list1[i]," "),end=" ")
   print('')
   