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
print(sum_even)
print(sum_odd)