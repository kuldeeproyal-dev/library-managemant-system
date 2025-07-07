# 📚 Library Management System (Python CLI)

A simple **Library Management System** built using **Python** and **Pandas**, designed for beginners. It allows users to borrow, return, search, and donate books using data from a CSV file.

---

## ⚙️ Features

* ✅ Borrow a book (with 14-day return policy and fine after due date)
* 🔄 Return a book (with fine calculation)
* 🔍 Search for books by title or author
* 🡩‍💻 Display all authors
* 📅 Donate books to the library
* 🗃️ Loads book data from `books.csv`
* 📦 Data managed in memory using **Pandas**

---

## 🗂️ Project Structure

```
📁 library-management/
├── books.csv              # Book dataset file
├── library-management.py # Main Python script
└── README.md              # Project overview
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/library-management.git
cd library-management
```

### 2. Install Dependencies

Make sure you have Python 3.11+ installed.

Install required Python packages:

```bash
pip install pandas
```

### 3. Run the Application

```bash
python library-management.py
```

---

## 📌 Notes

* The CSV file should have the following columns:

  * `title`
  * `authors`
  * `available_copies` *(added automatically if missing)*
  * `borrow_date` *(added automatically if missing)*

* Fine is ₹5 per day after the 14-day borrowing period.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest features.

---

## 📜 License

This project is licensed under the MIT License.
