print("-------Welcome to your daily journals------")
print("What would you like to do today?")

date = input("Enter the date in yyyy-mm-dd format: ")
notes = input("Enter your notes (max 4000 chars allowed):\n")

content = f"{date} -> {notes}"

with open("files/log.txt", "r") as file:
    journal = file.readlines()

journal.append(content + "\n")

with open("files/log.txt", 'w') as file:
    file.writelines(journal)


for note in journal:
    print(note)

