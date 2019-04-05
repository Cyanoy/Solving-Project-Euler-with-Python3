N1, N2, Temp, Sum = 1, 1, 0, 0
while Temp <= 4000000 :
    Sum += Temp
    N1 = N2 + Temp
    N2 = N1 + Temp
    Temp = N1 + N2
print(Sum)
