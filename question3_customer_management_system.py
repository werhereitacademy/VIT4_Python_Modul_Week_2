# Define a dictionary to store customer information with unique IDs
customers = {}

# Function to add a new customer
def add_customer():
    print("Adding a new customer:")
    customer_id = input("Enter customer ID: ")
    if customer_id in customers:
        print("Customer ID already exists. Please try again.")
        return
    else:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        customers[customer_id] = {'First Name': first_name, 'Last Name': last_name, 'Email': email, 'Phone': phone}
        print("Customer added successfully.")

# Function to update customer information
def update_customer():
    print("Updating customer information:")
    customer_id = input("Enter customer ID: ")
    if customer_id in customers:
        print("Current information for customer", customer_id, ":", customers[customer_id])
        first_name = input("Enter new first name (leave blank to keep current): ")
        if first_name:
            customers[customer_id]['First Name'] = first_name
        last_name = input("Enter new last name (leave blank to keep current): ")
        if last_name:
            customers[customer_id]['Last Name'] = last_name
        email = input("Enter new email (leave blank to keep current): ")
        if email:
            customers[customer_id]['Email'] = email
        phone = input("Enter new phone (leave blank to keep current): ")
        if phone:
            customers[customer_id]['Phone'] = phone
        print("Customer information updated successfully.")
    else:
        print("Customer ID not found.")

# Function to delete a customer
def delete_customer():
    print("Deleting a customer:")
    customer_id = input("Enter customer ID: ")
    if customer_id in customers:
        del customers[customer_id]
        print("Customer deleted successfully.")
    else:
        print("Customer ID not found.")

# Function to list all customers
def list_customers():
    print("Listing all customers:")
    if customers:
        for customer_id, customer_info in customers.items():
            print("Customer ID:", customer_id)
            for key, value in customer_info.items():
                print(key + ':', value)
            print('--------------------------')
    else:
        print("No customers found.")

# Main function to display menu and handle user choices
def main():
    while True:
        print("\nCustomer Management System Menu:")
        print("1. Add a new customer")
        print("2. Update customer information")
        print("3. Delete a customer")
        print("4. List all customers")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_customer()
        elif choice == '2':
            update_customer()
        elif choice == '3':
            delete_customer()
        elif choice == '4':
            list_customers()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

    main()
