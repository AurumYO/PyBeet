#Ex. 1: Dict comprehension exercise. Make a program that given a whole sentence (a string) will make a dict containing
# all unique words as keys and the number of occurrences as values.
sent = str(input("Please write your sentence here: "))
li_sent = sent.split(' ')
sen_di = {}
for k in li_sent:
    v = 1
    if k not in sen_di:
        sen_di[k] = v
    elif k in sen_di:
        sen_di[k] += 1
print(sen_di)

#Ex. 2: List comprehension exercise I.Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Now, make a program (no longer than 1 line) that makes a new list containing all the values in a but no even numbers.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("Second solution:")
ali = [i for i in a if i %2 != 0]
print(ali)
print("First solution:")
new_a = []
for i in a:
    if i % 2 != 0:
        new_a.append(i)
print(new_a)

#Ex2: List comprehension exercise II. Use a list comprehension to make a list containing tuples (i, j)
# where i goes from 1 to 10 and j is corresponding i squared.
list_a = [i for i in range(1, 11)]
list_b = [j ** 2 for j in list_a]
tup = tuple(zip(list_a,list_b))
print(tup)