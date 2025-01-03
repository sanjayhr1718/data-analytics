import sqlite3

class StudentDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("student_database.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                course TEXT
            )
        """)
        self.conn.commit()

    def add_student(self, name, age, course):
        self.cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
        self.conn.commit()
        print(f"Student '{name}' added successfully.")

    def display_students(self):
        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        print("\n--- Student Records ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")

    def search_student(self, student_id):
        self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        record = self.cursor.fetchone()
        if record:
            print(f"\nStudent Found: ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}")
        else:
            print("\nStudent not found.")

    def update_student(self, student_id, name, age, course):
        self.cursor.execute(
            "UPDATE students SET name = ?, age = ?, course = ? WHERE id = ?",
            (name, age, course, student_id)
        )
        self.conn.commit()
        print("\nStudent record updated successfully.")

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        self.conn.commit()
        print("\nStudent record deleted successfully.")

    def close_connection(self):
        self.conn.close()

def student_menu():
    db = StudentDatabase()
    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            db.add_student(name, age, course)
        elif choice == '2':
            db.display_students()
        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            db.search_student(student_id)
        elif choice == '4':
            student_id = int(input("Enter student ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            db.update_student(student_id, name, age, course)
        elif choice == '5':
            student_id = int(input("Enter student ID to delete: "))
            db.delete_student(student_id)
        elif choice == '6':
            db.close_connection()
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    student_menu()
