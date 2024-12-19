f = open("input.txt", "r")

list1 = []
list2 = []
distance = 0;

for x in f:
  list_items = x.split()
  list1.append(int(list_items[0]))
  list2.append(int(list_items[1]))
  
list1.sort()
list2.sort()

for index, item in enumerate(list1):
  distance += abs(list1[index] - list2[index]);

print(distance) #2378066 = correct answer