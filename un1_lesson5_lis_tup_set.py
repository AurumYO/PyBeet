##Exclusive common numbers. Generate 2 lists of length 10 with random integers from 1 to 10, and make
# a third list containing the common integers between the 2 initial lists without any duplicates.
print("Ex#1: Exclusive common numbers")
import random
ali = [random.randrange(1, 11) for _ in range(0, 10)]
bili = [random.randrange(1, 11) for _ in range(0, 10)]
tili = []
print(ali)
print(bili)
for x in ali:
  if x in ali and x in bili and x not in tili:
    tili.append(x)
  else:
    continue
print(tili)

#Make a list that contains all integers from 1 to 100, then find all integers from the list that
#are divisible by 7 but not a multiple of 5 and store them in a separate list.
# Finally print the list.
print("Ex#2: Extracting numbers")
import random
li = [random.randint(0, 101, ) for _ in range(0, 100)]
new_li = []
for x in li:
  if x % 7 == 0 and x % 5 != 0:
      if x not in new_li:
        new_li.append(x)
  else:
    continue
print(new_li)
