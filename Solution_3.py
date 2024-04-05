customers = {}

while True:
    print("Menu:")
    print("1. Add a new customer")
    print("2. Update customer information")
    print("3. Delete a customer")
    print("4. List all customers")
    print("5. Exit")
    
    choice = input("Select an operation (1-5): ")
    
    if choice == '1':
        customer_id = input("Enter customer ID: ")
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        email = input("Enter customer's email address: ")
        phone = input("Enter customer's phone number: ")
        
        customer_info = {'First Name': first_name, 'Last Name': last_name, 'Email': email, 'Phone': phone}
        customers[customer_id] = customer_info
        print("New customer added.")
    elif choice == '2':
        customer_id = input("Enter customer ID to update: ")
        if customer_id in customers:
            print("Current customer information:")
            print(customers[customer_id])
            first_name = input("Enter new first name (Leave empty if you don't want to change): ")
            last_name = input("Enter new last name (Leave empty if you don't want to change): ")
            email = input("Enter new email address (Leave empty if you don't want to change): ")
            phone = input("Enter new phone number (Leave empty if you don't want to change): ")
            
            if first_name:
                customers[customer_id]['First Name'] = first_name
            if last_name:
                customers[customer_id]['Last Name'] = last_name
            if email:
                customers[customer_id]['Email'] = email
            if phone:
                customers[customer_id]['Phone'] = phone
            
            print("Customer information updated.")
        else:
            print("Customer not found.")
    elif choice == '3':
        customer_id = input("Enter customer ID to delete: ")
        if customer_id in customers:
            del customers[customer_id]
            print("Customer deleted.")
        else:
            print("Customer not found.")
    elif choice == '4':
        if customers:
            for customer_id, customer_info in customers.items():
                print(f"Customer ID: {customer_id}, First Name: {customer_info['First Name']}, Last Name: {customer_info['Last Name']}, Email: {customer_info['Email']}, Phone: {customer_info['Phone']}")
        else:
            print("No customers found.")
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
