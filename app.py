def full_name():
    try:
        first_name = input("Enter your first name: ")
        if not first_name:
            raise ValueError("Give first name yarrr.")
        
        last_name = input("Enter your last name: ")
        if not last_name:
            raise ValueError("Give last name yarrs.")
        
        full_name = first_name + " " + last_name
        print(f"Full name: {full_name}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

# Run the function
full_name()
