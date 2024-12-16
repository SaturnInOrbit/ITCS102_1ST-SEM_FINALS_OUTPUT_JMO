def activity23():
    number = int(input("Enter the number you want to factor: "))
    print("\n\t========================== ACTIVITY 23 ==========================\n")
    
    # Initialize factorial to 1
    fact = 1
    
    # Calculate factorial
    for x in range(number, 0, -1):
        fact *= x  # Multiply fact by the current value of x
    
    print(f"The factorial of {number} is: {fact}")
    return fact

activity23()
"""SO ACTIVITY 23 IS DOCUMENT STRINGS LANG. LIKE HOW ALL DEF SHOULD HAVE IT"""