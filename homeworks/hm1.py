fruit = ["apple", "Orange", "Mandarin", "banana", "strawberry", "apricot"]
total = len(fruit)
half = int(total / 2)
halflist1 = fruit[:half]
a = halflist1
halflist2 = fruit[half:]
halflist1 = halflist2
halflist2 = a
fruit = halflist1 + halflist2
for i in fruit:
    print(i)


