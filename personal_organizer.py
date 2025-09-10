#------------------------------
#------Personal Organizer------
#------------------------------

tasks = []
notes = []
contacts = []

#---------------TASKS FUNCTION--------------------
def add_tasks():
    task = input("Add a new task: ")
    tasks.append(task)
    print("Task added")

def show_tasks():
    if not tasks:
        print("No tasks found")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")

def delete_task():
    show_tasks()
    if tasks:
        try:
            num = int(input("Enter number of task to delete: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' deleted")
            else:
                print("Invalid number")
        except ValueError:
            print("Enter the right number")

#----------------NOTES FUNCTION---------------------
def add_note():
    note = input("Add a note: ")
    notes.append(note)
    print("A note added") 

def show_notes():
    if not notes:
        print("No notes found")
    else:
        for i, n in enumerate(notes, 1):
            print(f"{i}. {n}")

def delete_note():
    show_notes()
    if notes:
        try:
            num = int(input("Enter number of note to delete: "))
            if 1 <= num <= len(notes):
                removed = notes.pop(num - 1)
                print(f"Note '{removed}' deleted")
            else:
                print("Invalid number")
        except ValueError:
            print("Enter the right number")

#---------------CONTACT FUNCTION---------------
def add_contacts():
    name = input("Add Contact Name: ")
    phone = input("Add phone number: ")
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added")

def show_contacts():
    if not contacts:
        print("No contacts found")
    else:
        for i, c in enumerate(contacts, 1):
            print(f"{i}. {c['name']} - {c['phone']}")
    
def delete_contacts():
    show_contacts()
    if contacts:
        try:
            num = int(input("Enter number of Contact to delete: "))
            if 1 <= num <= len(notes):
                removed = notes.pop(num - 1)
                print(f"{removed['name']} - {removed['phone']} deleted")
            else:
                print("Invalid number")
        except ValueError:
            print("Enter the right number")

while True:
    print("-------Personal Organizer---------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Add Note")
    print("5. View Notes")
    print("6. Delete Note")
    print("7. Add Contact")
    print("8. View Contacts")
    print("9. Delete Contact")
    print("10. Exit")

    choice = input("Choose (1-10): ")

    if choice == "1":
        add_tasks()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        add_note()
    elif choice == "5":
        show_notes()
    elif choice == "6":
        delete_note()
    elif choice == "7":
        add_contacts()
    elif choice == "8":
        show_contacts()
    elif choice == "9":
        delete_contacts()
    elif choice == "10":
        print("Exiting")
        break
    else:
        print("Invalid Choice")