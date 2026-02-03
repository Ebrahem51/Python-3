contacts = {}

contacts["Ahmed"] = "01234567890"
contacts["Sara"] = "01112223344"
contacts["Mohamed"] = "01005556677"

print("===== Contact Book =====")

print("\nAll contacts:")
for name in contacts.keys():
    print(f"- {name}")

print("\n--- Search for a contact ---")
search_name = input("Enter name to search: ")

if search_name in contacts:
    print(f"{search_name}'s phone number is: {contacts[search_name]}")
else:
    print(f"Sorry, '{search_name}' is not in the contact book.")