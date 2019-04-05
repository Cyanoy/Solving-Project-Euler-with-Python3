N1, N2, Temp, Sum = 1, 1, 0, 0
while Temp <= 4000000 :
    if Temp%2 == 0 :
        Sum += Temp
    Temp = N1 + N2
    N1 = N2
    N2 = Temp
print(Sum)
