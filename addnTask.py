import csv

# Function to load and return the CSV data
def load_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            data.append(row)
    return data

# Function to filter data based on user choice
def filter_data(data, choice):
    if choice == 1:
        filtered_books = [book for book in data if float(book['Price'].replace(',', '.')) <= 150]
    elif choice == 2:
        filtered_books = [book for book in data if int(book['Year-Of-Publication']) <= 2016]
    elif choice == 3:
        filtered_books = [book for book in data if int(book['Year-Of-Publication']) in [2014, 2016, 2017]]
    elif choice == 4:
        filtered_books = [book for book in data if float(book['Price'].replace(',', '.')) <= 200]
    elif choice == 5:
        filtered_books = data  # No filter
    elif choice == 6:
        filtered_books = [book for book in data if float(book['Price'].replace(',', '.')) >= 150]
    elif choice == 7:
        filtered_books = [book for book in data if 2016 <= int(book['Year-Of-Publication']) <= 2018]
    elif choice == 8:
        filtered_books = [book for book in data if int(book['Year-Of-Publication']) in [2015, 2018]]
    elif choice == 9:
        filtered_books = [book for book in data if float(book['Price'].replace(',', '.')) >= 200]
    elif choice == 10:
        filtered_books = [book for book in data if int(book['Year-Of-Publication']) >= 2018]
    else:
        filtered_books = []

    return filtered_books[:20]  # Limit to the top 20 books

# Main program
if __name__ == "__main__":
    file_path = 'books-en.csv'
    books_data = load_csv(file_path)
    valid_choices = set(range(1, 11))

    while True:
        # Display filtering options
        print("Filtering Options:")
        print("1. Up to 150 rubles")
        print("2. Until 2016")
        print("3. Only 2014, 2016, and 2017")
        print("4. Up to 200 rubles")
        print("5. No Filter")
        print("6. From 150 rubles")
        print("7. From 2016 to 2018")
        print("8. Only 2015 and 2018")
        print("9. From 200 rubles")
        print("10. From 2018")
        print("0. Exit")

        # Get user choice
        user_choice = int(input("Choose an option (0-10): "))

        if user_choice == 0:
            break

        if user_choice not in valid_choices:
            print("Invalid choice. Please choose a number between 1 to 10")
        else:
            filtered_books = filter_data(books_data, user_choice)

            # Display filtered results
            if not filtered_books:
                print("No books match the selected criteria.")
            else:
                print("Top 20 Books:")
                for index, book in enumerate(filtered_books, start=1):
                    print(
                        f"{index}. ISBN: {book['ISBN']}, Title: {book['Book-Title']}, Author: {book['Book-Author']}, Price: {book['Price']} rubles")

