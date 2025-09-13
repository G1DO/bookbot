# 📚 BookBot  

BookBot is my first [Boot.dev](https://www.boot.dev) project! 🚀  

It analyzes books (plain text files) and prints a report of:  
- Total word count  
- Character frequency (sorted from most common to least)  

---

## ⚡ Features  
- Reads any `.txt` book file  
- Counts total words  
- Counts each character frequency (case-insensitive)  
- Outputs a clean statistical report in the terminal  
- Works with multiple books (Frankenstein, Moby Dick, Pride and Prejudice, etc.)  

---

## 🛠️ Installation & Usage  

1. Clone this repository:  
   ```bash
   git clone https://github.com/YOUR-USERNAME/bookbot.git
   cd bookbot
Run BookBot with a book file:

bash
Copy code
python3 main.py books/frankenstein.txt
Example output:

diff
Copy code
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
-------- Character Count --------
e: 44538
t: 29493
a: 25894
...
============= END ===============
📂 Project Structure
bash
Copy code
bookbot/
│── books/                # Book text files (ignored in Git)
│── main.py               # Entry point
│── stats.py              # Functions for analysis
│── README.md             # Documentation
│── .gitignore            # Ignore books folder
