from datetime import date
import os

print("-------Welcome to your daily journals------")
current_date = date.today()
display_day = current_date.strftime("%A")
display_date = current_date.strftime("%d-%B-%Y")
file_format_date = current_date.strftime("%Y_%m_%d")
print(f"Today is {display_date}, a {display_day}")

print("Start recording your journals for the day")
print("Enter your notes here (type 'done' when you are finished recording: ")

journals = []
journal_num = 1
entries = ""

while entries.lower() != "done":
    entries = input(f"Journal {journal_num}: ").strip()
    if entries.lower() != "done":
        journals.append(entries + "\n")
        journal_num += 1

notes_directory = "files"
if not os.path.exists(notes_directory):
    os.makedirs(notes_directory)

filename = f"{notes_directory}/journals_{file_format_date}.txt"

try:
    print("Writing journals to file.....")
    with open(filename, "a") as file:
        file.writelines(journals)
    print("Entries Saved Successfully!")
    print(f"Saved {len(journals)} entries to {filename}")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
    raise SystemExit(1)  # Exit the program if writing fails

