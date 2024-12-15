sum = 0
sum_even = 0
sum_odd = 0
for x in range(1,11):
    num = eval(input(f"Enter #{x}:"))
    sum += num
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print(f"The sum of all numbers given is {sum}")
print(f"The sum of all even numbers given is {sum_even}")
print(f"The sum of all numbers given is {sum_odd}")