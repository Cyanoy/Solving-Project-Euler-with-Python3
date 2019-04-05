Num , Sum = 1 , 0
Multiples = []
while Num < 1000 :
    if Num % 3 == 0 :
        Sum += Num
        Multiples.append(Num)
    elif Num % 5 == 0 :
        Sum += Num
        Multiples.append(Num)
    Num = Num + 1
print('The sum of the multiples are ' + str(Sum) )
print(Multiples)
