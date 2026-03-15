from database import Database
from student import Student
from analytics import Analytics
from utils import safe_run


class Controller:

    def __init__(self):
        self.db = Database()
        self.records = self.db.read()

    @safe_run
    def add_student(self):
        sid = input("Enter student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        grade = input("Grade: ")

        subjects = {}
        for sub in ["Maths", "Physics", "Chemistry", "English", "Computer"]:
            subjects[sub] = int(input(f"{sub} marks: "))

        self.records[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects,
        }

        self.db.write(self.records)
        print("✔ Student added!\n")

    @safe_run
    def view_all(self):
        for sid, info in self.records.items():
            print(Student(sid, **info))
        print()

    @safe_run
    def update_student(self):
        sid = input("Enter ID to update: ")

        if sid not in self.records:
            print("ID not found")
            return

        info = self.records[sid]

        name = input(f"Name ({info['name']}): ") or info["name"]
        age = input(f"Age ({info['age']}): ") or info["age"]
        grade = input(f"Grade ({info['grade']}): ") or info["grade"]

        subjects = {}
        for sub in info["subjects"]:
            old = info["subjects"][sub]
            new = input(f"{sub} ({old}): ")
            subjects[sub] = int(new) if new else old

        self.records[sid] = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects,
        }

        self.db.write(self.records)
        print("✔ Updated!\n")

    @safe_run
    def delete_student(self):
        sid = input("Enter ID to delete: ")

        if sid in self.records:
            del self.records[sid]
            self.db.write(self.records)
            print("✔ Deleted!\n")
        else:
            print("ID not found.")

    @safe_run
    def show_toppers(self):
        topper = Analytics.topper(self.records)
        print(f"🏆 Overall Topper: {topper}")

        for subj in ["Maths", "Physics", "Chemistry", "English", "Computer"]:
            print(f"⭐ {subj} topper: {Analytics.subject_topper(self.records, subj)}")

        print()

    @safe_run
    def show_dataframe(self):
        df = Analytics.dataframe(self.records)
        print(df, "\n")


def menu():
    app = Controller()

    while True:
        print("\n===== STUDENT MANAGER =====")
        print("1. Add Student")
        print("2. View All")
        print("3. Update")
        print("4. Delete")
        print("5. Show Toppers")
        print("6. Show DataFrame")
        print("7. Exit")

        ch = input("Choice: ")

        if ch == "1":
            app.add_student()
        elif ch == "2":
            app.view_all()
        elif ch == "3":
            app.update_student()
        elif ch == "4":
            app.delete_student()
        elif ch == "5":
            app.show_toppers()
        elif ch == "6":
            app.show_dataframe()
        elif ch == "7":
            break
        else:
            print("Invalid choice\n")


if __name__ == "__main__":
    menu()
