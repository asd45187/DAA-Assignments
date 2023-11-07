def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

nterms = 10

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))



## Non Recurive 

first = 0
second = 1
n = 10

print(first)
print(second)

for i in range(1, n - 1):  # Adjust the range to generate 'n' terms
    third = first + second
    first, second = second, third
    print(third)
