def biodata():
    full_name = input("Please enter your full name: ")
    gen = input("Please enter your gender: ")
    age = input("Please enter your age: ")
    Fname = input("Please enter your father's full name: ")
    Mname = input("Please enter your mother's maiden name: ")
    nat = input("Enter your nationality: ")
    bdate = input("Enter your date of birth: ")
    bplace = input("Enter your place of birth: ")
    cstat = input("Enter your civil status: ")
    rel = input("Enter your religion: ")
    skill = input("Enter your relevant skills: ")
    hobby = input("Enter your hobbies: ")
    email = input("Please enter a valid e-mail address: ")
    mobile = input("Please enter your mobile number: ")

    # Print using an f-string
    print(
        f"Hi! I'm {full_name}. I am {gen} and I am {age} years old. "
        f"My parents are {Fname} and {Mname}. I am {nat} and was born on {bdate} at {bplace}, "
        f"and I am currently {cstat}. My religion is {rel} and I am proficient in {skill}. "
        f"Not only that, but I also like to do {hobby} in my free time. "
        f"If you have any more questions about me, you can contact me through {email} or {mobile}. "
        "That's all about me. Thank you!"
    )

# Call the function
biodata()