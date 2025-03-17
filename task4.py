CONTACTS = {}


def add_contact(name, phone):
    CONTACTS[name] = phone
    
def change_contact(name, phone):    
    if name in CONTACTS:
        CONTACTS[name] = phone
    else:
        print(f"Contact {name} not found")  

def get_contact(name):  
    if name in CONTACTS:
        return f"Phone: {CONTACTS[name]}"
    else:
        return f"Contact {name} not found"  

def main():
   print("Welcome to the assistant bot!\nYou can use command hello, add, change, phone or exit/close")
   while True:
        user_response = input(f"Please input command:").strip().lower()
        if user_response == "hello":
            print("How can I help you?\n You can use command hello, add, change, phone or exit/close")
        elif user_response == "add":
            name = input("Please input name: ")
            phone = input("Please input phone: ")
            add_contact(name, phone)
        elif user_response == "change":
            name = input("Please input name: ")
            phone = input("Please input phone: ")
            change_contact(name, phone)
        elif user_response == "phone":
            name = input("Please input name: ")
            print(get_contact(name))
        elif user_response == "exit" or user_response == "close":
            print(f"Goodbye!")
            break 
        else:
            print("Command not found! Please try again")

if __name__ == "__main__":
    main() # Call main function