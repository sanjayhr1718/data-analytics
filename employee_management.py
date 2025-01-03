import sqlite3

class EmployeeDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("employee_database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT,
                salary REAL
            )
        """)
        self.conn.commit()

    def add_employee(self, name, position, salary):
        self.cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
        self.conn.commit()
        print(f"Employee '{name}' added successfully.")

    def display_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        rows = self.cursor.fetchall()
        print("\n--- Employee Records ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Position: {row[2]}, Salary: {row[3]}")

    def search_employee(self, employee_id):
        self.cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
        record = self.cursor.fetchone()
        if record:
            print(f"\nEmployee Found: ID: {record[0]}, Name: {record[1]}, Position: {record[2]}, Salary: {record[3]}")
        else:
            print("\nEmployee not found.")

    def update_employee(self, employee_id, name, position, salary):
        self.cursor.execute(
            "UPDATE employees SET name = ?, position = ?, salary = ? WHERE id = ?",
            (name, position, salary, employee_id)
        )
        self.conn.commit()
        print("\nEmployee record updated successfully.")

    def delete_employee(self, employee_id):
        self.cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
        self.conn.commit()
        print("\nEmployee record deleted successfully.")

    def close_connection(self):
        self.conn.close()

def employee_menu():
    db = EmployeeDatabase()
    while True:
        print("\n--- Employee Management Menu ---")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = float(input("Enter salary: "))
            db.add_employee(name, position, salary)
        elif choice == '2':
            db.display_employees()
        elif choice == '3':
            employee_id = int(input("Enter employee ID: "))
            db.search_employee(employee_id)
        elif choice == '4':
            employee_id = int(input("Enter employee ID: "))
            name = input("Enter new name: ")
            position = input("Enter new position: ")
            salary = float(input("Enter new salary: "))
            db.update_employee(employee_id, name, position, salary)
        elif choice == '5':
            employee_id = int(input("Enter employee ID to delete: "))
            db.delete_employee(employee_id)
        elif choice == '6':
            db.close_connection()
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    employee_menu()
