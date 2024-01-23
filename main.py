from functions import *
def main():
    conn = connect_to_database()
    role = input("Enter your role (1 for Admin, 2 for User): ")

    while True:
        print("\nOperations:")
        print("1. Insert Data")
        print("2. Update Data")
        print("3. Delete Data")
        print("4. Display Data")
        print("5. Exit")

        operation = input("Enter the operation number you want to perform: ")

        if operation == '1' and role == '1' :  # Insert Data
            Company_ID = input("Enter the Company_ID: ")
            Ticker = input("Enter name: ")
            Open = float(input("Enter the Open value: "))
            High = float(input("Enter the High value: "))
            Low = float(input("Enter the Low value: "))
            Close = float(input("Enter the Close value: "))
            Adjclose = float(input("Enter the Adjclose value: "))
            Volume = int(input("Enter the Volume value: "))

            insert_data(conn, Company_ID, Ticker, Open, High, Low, Close, Adjclose, Volume)
            print("Data inserted successfully.")

        elif operation == '2' and role == '1':  # Update Data
            Company_ID = input("Enter Company_ID to update: ")
            New_Company = input("Enter the New_Company: ")

            update_data(conn, Company_ID, New_Company)
            print("Data updated successfully.")

        elif operation == '3' and role == '1':  # Delete Data
            Company_ID = input("Enter Company_ID to delete: ")

            delete_data(conn, Company_ID)
            print("Data deleted successfully.")

        elif operation == '4':  # Display Data
            data = select_data(conn)
            print("Table:")
            print(data)
            
        elif operation == '5':  # Exit
            break

        else:
            print("Invalid operation. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()