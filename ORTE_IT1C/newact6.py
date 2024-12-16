def operator():
    x = 5
    # Get 5 inputs and convert them to integers
    num = [int(input(f"Enter a number #{i + 1}: ")) for i in range(5)]
    
    # Print each operation
    print(f"x += {num[1]}")
    x += num[1]
    print(f"x = {x}")
    print("")
    print(f"x -= {num[2]}")
    x -= num[2]
    print(f"x = {x}")
    print("")
    print(f"x *= {num[3]}")
    x *= num[3]
    print(f"x = {x}")
    print("")
    print(f"x //= {num[4]}")
    x //= num[4]
    print(f"x = {x}")

# Call the operator function
operator()

