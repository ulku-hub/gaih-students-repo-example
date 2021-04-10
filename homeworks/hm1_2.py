number = input(" Please enter a single digit number:  ")

try:
    if  int(number)>=0 :
        print("çift sayılar")
        for i in range(int(number)):
             if i % 2 == 0:
                print(i)


except:
        print(" Please enter a single digit number:  ")