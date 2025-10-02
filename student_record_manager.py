class Student:
    def __init__(self, roll, name, grade):
        self.roll = roll
        self.name = name
        self.grade = grade 
    
    def display(self):
        return f"Roll : {self.roll}, Name: {self.name}, Grade: {self.grade}"
    
class student_record_manager:

    def __init__(self):
        self.records = {}

    def add_student(self, roll, name, grade):
        if roll in self.records:
            print("Student already in the records")
        else:
            self.records[roll] = Student(roll, name, grade)
            print(f"Added {name}")

    def get_student(self, roll):
        if roll in self.records:
            return self.records[roll].display()
        else: 
            return "Student Not Found"
        
    def update_student(self, roll, name = None, grade = None):
        if roll in self.records:
            if name:
                self.records[roll].name = name
            if grade:
                self.records[roll].grade = grade
            print("Student Updated")
        else:
            print("Student not in the records")

    def show_all(self):
        if not self.records:
            print("No records found")
        else:
            for student in self.records.values():
                print(student.display())
    
    def delete_student(self, roll):
        if roll in self.records:
            del self.records[roll]
            print("Student Deleted")
        else:
            print("Student not in the records")

manager = student_record_manager()

while True:
    print("\n--- Student Record Manager ---")
    print("1. Add student")
    print("2. Get student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Show all")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        # Add student
        roll = input("Enter roll: ").strip()
        name = input("Enter name: ").strip()
        grade = input("Enter grade: ").strip()
        manager.add_student(roll, name, grade)

    elif choice == "2":
        # Get student
        roll = input("Enter roll to fetch: ").strip()
        print(manager.get_student(roll))

    elif choice == "3":
        # Update student
        roll = input("Enter roll to update: ").strip()
        name = input("Enter new name (leave blank if no change): ").strip()
        grade = input("Enter new grade (leave blank if no change): ").strip()
        # Convert empty strings to None
        name = name if name else None
        grade = grade if grade else None
        manager.update_student(roll, name, grade)

    elif choice == "4":
        # Delete student
        roll = input("Enter roll to delete: ").strip()
        manager.delete_student(roll)

    elif choice == "5":
        # Show all students
        manager.show_all()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter a number from 1-6.")

