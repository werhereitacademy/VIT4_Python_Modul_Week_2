#question 3 CustomerManagementSystem:
class CustomerManagementSystem:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer_id, name, surname, email, phone):
        if customer_id not in self.customers:
            self.customers[customer_id] = {"name": name, "surname": surname, "email": email, "phone": phone}
            print("Customer added successfully.")
        else:
            print("Customer ID already exists. Please choose a unique ID.")

    def update_customer(self, customer_id, name=None, surname=None, email=None, phone=None):
        if customer_id in self.customers:
            customer = self.customers[customer_id]
            if name:
                customer["name"] = name
            if surname:
                customer["surname"] = surname
            if email:
                customer["email"] = email
            if phone:
                customer["phone"] = phone
            print("Customer information updated successfully.")
        else:
            print("Customer ID not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print("Customer deleted successfully.")
        else:
            print("Customer ID not found.")

    def list_customers(self):
        if self.customers:
            print("List of Customers:")
            for customer_id, customer_info in self.customers.items():
                print(f"ID: {customer_id}, Name: {customer_info['name']}, Surname: {customer_info['surname']}, Email: {customer_info['email']}, Phone: {customer_info['phone']}")
        else:
            print("No customers in the system.")

# Main program
cms = CustomerManagementSystem()
while True:
    print("\nCustomer Management System")
    print("1. Add Customer")
    print("2. Update Customer")
    print("3. Delete Customer")
    print("4. List Customers")
    print("5. Exit")
    choice = input("Enter the number of the action you want to perform: ")

    if choice == "1":
        customer_id = input("Enter Customer ID: ")
        name = input("Enter Name: ")
        surname = input("Enter Surname: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        cms.add_customer(customer_id, name, surname, email, phone)
    elif choice == "2":
        customer_id = input("Enter Customer ID: ")
        name = input("Enter New Name (Leave blank to keep the old value): ")
        surname = input("Enter New Surname (Leave blank to keep the old value): ")
        email = input("Enter New Email (Leave blank to keep the old value): ")
        phone = input("Enter New Phone (Leave blank to keep the old value): ")
        cms.update_customer(customer_id, name, surname, email, phone)
    elif choice == "3":
        customer_id = input("Enter Customer ID: ")
        cms.delete_customer(customer_id)
    elif choice == "4":
        cms.list_customers()
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")