import datetime


class notes:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def format(self):
        return f"[{self.date}] {self.title}\n{self.body}\n\n"
    
def add_notes():
    title = input("Enter Title: ")
    body = input("Enter body: ")
    note = notes(title, body)
    with open("notess.txt", "a") as f:
        f.write(note.format())
    return "Note Saved"

def view_notes():
    try:
        with open("notess.txt", "r") as f:
            content = f.read().strip()
            if content:
                print("Your Notes:")
                print(content)
            else:
                print("No notes yet.")
    except FileNotFoundError:
        print("notess.txt not found- add a note first")
    
def main():
    while True:
        print("\n 1. Add Note \n 2. View Notes\n 3. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_notes()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("See ya!")
            break
        else:
            print("Invalid Choice")



if __name__ == "__main__":
    main()