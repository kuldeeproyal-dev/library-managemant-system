import pandas as pd
from datetime import datetime, timedelta

def load_books_data():
    try:
        df = pd.read_csv('books.csv', on_bad_lines='skip')  # Skips rows with errors
    except Exception as e:
        print(f"Error loading CSV: {e}")
        exit()
    if 'available_copies' not in df.columns:
        df['available_copies'] = 5
    if 'borrow_date' not in df.columns:
        df['borrow_date'] = ""
    return df

def show_menu():
    print("\n---Library Menu---")
    print("1. Borrow a book")
    print("2. Return a book")
    print("3. Search book availability")
    print("4. Search by author")
    print("5. Donate a book")
    print("6. Exit")

def take_book(df):
    print("\nHow would you like to search?")
    print("1. By Title")
    print("2. By Author")
    search_choice = input("Enter choice (1/2): ")

    if search_choice == '1':
        query = input("Enter book title: ").strip().lower()
        results = df[df['title'].str.lower().str.contains(query, na=False)]
    elif search_choice == '2':
        query = input("Enter author name: ").strip().lower()
        results = df[df['authors'].str.lower().str.contains(query, na=False)]
    else:
        print("Invalid choice. Please try again.")
        return

    if results.empty:
        print("No matching books found.")
        return

    print("\n📚 Matching Books:")
    print(results[['title', 'authors', 'available_copies']].head(10))
    book_borrowTitle = input("Enter the title to borrow (partial or full): ").strip().lower()
    matches = results[results['title'].str.lower().str.contains(book_borrowTitle, na=False)]
    if matches.empty:
            print("Book not found. Please try again.")
            return
    else:
            idx = matches.index[0]
            if df.at[idx, 'available_copies'] > 0:
                df.at[idx, 'available_copies'] -= 1
                df.at[idx, 'borrow_date'] = datetime.now().strftime('%Y-%m-%d')
                print(f"✅ You have successfully borrowed '{matches['title'].values[0]}' by {matches['authors'].values[0]}.")
                print(f"Return it by: {(datetime.now() + timedelta(days=14)):%Y-%m-%d} to avoid penalties.")
            else:
                print("Sorry, this book is currently not available.")

def return_book(df):
    title = input("Enter the title to return: ").strip().lower()
    matches = df[df['title'].str.lower() == title]
    if not matches.empty:
        idx = matches.index[0]
        borrow_date_str = df.at[idx, 'borrow_date']
        if borrow_date_str:
            df.at[idx, 'available_copies'] += 1
            try:
                borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
                days = (datetime.now() - borrow_date).days
                df.at[idx, 'borrow_date'] = ""
                if days > 14:
                    fine = (days - 14) * 5
                    print(f"⏳ Returned after {days} days. Fine: ₹{fine}")
                else:
                    print(f"✅ Book returned on time in {days} days. No fine.")
            except ValueError:
                print("⚠️ Invalid borrow date format.")
        else:
            print("⚠️ No borrow record found. Book return accepted.")
    else:
        print("❌ Book not found.")

def search_available_books(df):
    print("\nSearch for a book:")
    print("1. By Title")
    print("2. By Author")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        keyword = input("Enter part of the title: ").strip().lower()
        result = df[df['title'].str.lower().str.contains(keyword, na=False)]
    elif choice == '2':
        keyword = input("Enter part of the author's name: ").strip().lower()
        result = df[df['authors'].str.lower().str.contains(keyword, na=False)]
    else:
        print("❌ Invalid choice.")
        return

    if result.empty:
        print("❌ No matching books found.")
    else:
        print("\n📚 Matching Books:")
        print(result[['title', 'authors', 'available_copies']].head(10))

def display_authors(df):
    unique_authors = df['authors'].dropna().str.lower().unique()
    print("📚 All authors:")
    for author in sorted(unique_authors):
        print(author.title())

def donate_book(df):
    bookTitle = input("Enter book title: ").strip()
    author = input("Enter author's name: ").strip()
    try:
        copies = int(input("Enter number of copies to donate: "))
    except ValueError:
        print("❌ Invalid number of copies.")
        return
    new_book = {
        'title': bookTitle,
        'authors': author,
        'available_copies': copies,
        'borrow_date': ''
    }
    df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
    print("🙏 Thank you for donating the book!")

def main():
    df = load_books_data()
    while True:
        show_menu()
        try:
            option = int(input("Select your option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            take_book(df)
        elif option == 2:
            return_book(df)
        elif option == 3:
            search_available_books(df)
        elif option == 4:
            display_authors(df)
        elif option == 5:
            donate_book(df)
        elif option == 6:
            print("Exiting the Application")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()