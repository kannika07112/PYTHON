# Program 4: Contact book using dictionary

contacts = {}

def add_contact(name, number):
    contacts[name] = number

def search_contact(name):
    return contacts.get(name, "Not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]

add_contact("Alice", "12345")
add_contact("Bob", "67890")
print("Alice:", search_contact("Alice"))
print("Bob:", search_contact("Bob"))
print("Contact List ",contacts)
delete_contact("Bob")
print("After deleting ",contacts)
