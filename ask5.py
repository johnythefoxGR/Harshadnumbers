Harshad = []
for i in range(1,1001):
    numbers = map(int,list(str(i)))
    sum=0
    for num in numbers:
        sum += num
    if (i/sum).is_integer():
        Harshad.append(i)
print(Harshad)
