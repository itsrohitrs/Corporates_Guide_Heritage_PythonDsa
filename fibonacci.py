def fibonacci(n):

    a=0
    b=1
    count = 0

    while count < n:
        print(a,end=" ")
        c = a + b
        a=b
        b=c
        count+=1

terms = int(input("enter the no.of terms"))
print(fibonacci(terms))