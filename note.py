import os

def new_note():
    title = input("Title: ")
    fname = f"{title}.txt"
    if os.path.exists(fname):
        print("Use a different title.")
        return
    content = input("Write something here: ")
    with open(f"{title}.txt", "w") as file:
        file.write(content)
def open_note():
    title = input("Enter a title you would like to open: ")
    try:
        with open(f"{title}.txt","r") as file:
            content = file.read()
            print(f"Content for '{title}': \n{content}")
    except FileNotFoundError:
        print(f"The note '{title}' is nonexistent.")
def delete_note():
    title = input("Enter a title you would like to delete: ")
    try:
        os.remove(f"{title}.txt")
        print(f"The note '{title}' is deleted.")
    except FileNotFoundError:
        print(f"The note '{title}' is nonexistent.")
        
while True:
    print("\n9's note program")
    print("1. New note")
    print("2. Open note")
    print("3. Delete note")
    print("4. Exit program")

    menu = input("Menu number: ")
    if menu == "1":
        new_note()
    elif menu == "2":
        open_note()
    elif menu == "3":
        delete_note()
    elif menu == "4":
        print("Goodbye.")
        break
    else:
        print("Invalid number.")
        break