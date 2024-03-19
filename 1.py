x = int (input("Enter the first number: "))
y = int (input("Enter the second number: "))
z = int (input("Enter the limit: "))

def sum_of_multiples(num1, num2, limit):
    total_sum = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 ==0:
            total_sum += i
    return total_sum

que = sum_of_multiples(x, y, z)

print(f"The sum of multiples of {x} or {y} up to {z} is {que}.")

