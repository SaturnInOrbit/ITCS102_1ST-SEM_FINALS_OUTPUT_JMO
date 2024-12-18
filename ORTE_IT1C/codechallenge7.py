def grocery_store():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    print("\nSelect from these items:")
    print("1. Lamb: 350")
    print("2. Sirloin: 450")
    print("3. Caviar: 1000")
    print("4. Truffle Oil: 1200")
    print("5. Foie Gras: 800")
    print("Enter '0' when you are done selecting items.")

    total = 0

    while True:
        item = int(input("\nEnter the number of the item you want to buy (or 0 to finish): "))
        if item == 1:
            total += 350
        elif item == 2:
            total += 450
        elif item == 3:
            total += 1000
        elif item == 4:
            total += 1200
        elif item == 5:
            total += 800
        elif item == 0:
            break
        else:
            print("Invalid selection. Please choose a valid number.")

    if total == 0:
        print("You didn't buy anything.")
        return

    tax_percentage = 15
    discount_percentage = 10

    tax = (total * tax_percentage) / 100
    total_with_tax = total + tax
    print(f"\nA tax of {tax_percentage}% is added, which is {tax:.2f}.")

    if age >= 60:
        discount = (total_with_tax * discount_percentage) / 100
        print(f"\nYou get a discount of {discount_percentage}% which is {discount:.2f}.")
        total_with_tax -= discount

    print(f"Your total amount is: {total_with_tax:.2f}")

    confirm = input(f"\n{name}, do you accept the charges? (yes/no): ")
    if confirm == "yes":
        print("Thank you for your purchase!")
    else:
        print("Purchase cancelled.")

grocery_store()