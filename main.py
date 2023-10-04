import csv
import random


# Counting the number of records
def count_records(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        count = sum(1 for row in reader)
    return count


# Counting the number of records whose Название field is longer than 30 characters
def count_long_names(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        count = sum(1 for row in reader if len(row[1]) > 30)
    return count


# Implementing a book search by author with a limit on issuance
def search_books(file_name):
    print("!! For Searching Books !! ")
    author = input("Enter the author's name: ")
    limit = int(input("Enter the issuance limit: "))

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        for row in reader:
            if row[2] == author and int(row[3]) <= limit:
                print(row)


# Implementing a bibliographic reference generator
def generate_references(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter=";")
        next(reader)
        selected_rows = random.sample(list(reader), 20)
    with open('references.txt', 'w') as file:
        for i, row in enumerate(selected_rows, start=1):
            reference = f"{row[2]}. {row[1]} - {row[3]}\n"
            file.write(f"{i}. {reference}")


# Usages
file_name = 'books-en.csv'
print(f"Number of records: {count_records(file_name)}")
print(f"Number of records with long Название: {count_long_names(file_name)}")
generate_references(file_name)
print("For Bibliographic References Check references.txt file\n")
search_books(file_name)

