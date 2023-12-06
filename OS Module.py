import os, time
todo = []
fileExists =True
try:
    f = open("todo.txt", "r")
    todo = eval(f.read())
    f.close()
except FileNotFoundError:
    fileExists = False
    print("No datafile found! Creating a new one...")
    time.sleep(1)
    f = open("todo.txt", "w")
    f.write(str(todo))
    f.close()
    print("Done!")
    time.sleep(1)

def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name > ")
    date = input("Date > ")
    priority = input("Priority > ").capitalize()
    todo.append({"name": name, "date": date, "priority": priority})
    print("Added!")

def view():
    time.sleep(1)
    os.system("clear")
    print("Name\t\tDate\t\tPriority")
    print("----\t\t----\t\t--------")
    for i in todo:
        print(i["name"] + "\t\t" + i["date"] + "\t\t" + i["priority"])
    input("Press enter to continue...")

def edit():
    time.sleep(1)
    os.system("clear")
    print("Name\t\tDate\t\tPriority")
    print("----\t\t----\t\t--------")
    for i in todo:
        print(i["name"] + "\t\t" + i["date"] + "\t\t" + i["priority"])
    name = input("Name > ")
    for i in todo:
        if i["name"] == name:
            todo.remove(i)
            name = input("Name > ")
            date = input("Date > ")
            priority = input("Priority > ").capitalize()
            todo.append({"name": name, "date": date, "priority": priority})
            print("Edited!")
            break
    else:
        print("Not found!")

def remove():
    time.sleep(1)
    os.system("clear")
    print("Name\t\tDate\t\tPriority")
    print("----\t\t----\t\t--------")
    for i in todo:
        print(i["name"] + "\t\t" + i["date"] + "\t\t" + i["priority"])
    name = input("Name > ")
    for i in todo:
        if i["name"] == name:
            todo.remove(i)
            print("Removed!")
            break
    else:
        print("Not found!")

def backup():
    dirname = "backup"
    fname = make_name()
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    relpath = "/".join((dirname, fname))
    try:
        os.rename("todo.txt", relpath)
    except FileNotFoundError:
        print("There is no datafile to backup!")

def make_name(length:int=16):
    return "".join(choice(ascii_lowercase) for _ in range(length + 1))

while True:
    os.system("clear")
    print("1. Add\n2. View\n3. Edit\n4. Remove\n5. Quit")
    choice = input("> ")
    if choice == "1":
        add()
    elif choice == "2":
        view()
    elif choice == "3":
        edit()
    elif choice == "4":
        remove()
    elif choice == "5":
        backup()
        f = open("todo.txt", "w")
        f.write(str(todo))
        f.close()
        break
    else:
        print("Invalid choice!")
        time.sleep(1)
        continue
