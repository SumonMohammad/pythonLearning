def addContact(contacts, name, phone=None, email= None):
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added / updated.")


def viewContact(contacts, name):
    c = contacts.get(name)
    if c:
        print(f"Name: {name}")
        if c['phone']:
            print(f"Phone: {c['phone']}")
        if c['email']:
            print(f"Email: {c['email']}")
    else:
        print(f"Contact {name} not found.")

def main():
    contacts = {}
    print("Add a new contact")
    # name = input("Enter name: ")
    # phone = input("Enter phone (or leave blank): ")     
    # email = input("Enter email (or leave blank): ")

    # addContact(contacts, name, phone or None, email or None)
    viewContact(contacts, input("Name").strip())

        



if __name__ == "__main__":
    main()
