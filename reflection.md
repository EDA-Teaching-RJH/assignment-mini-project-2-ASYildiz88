# Reflection – Mini Project 2

## Project Overview

This project focuses on analysing log data using Python. The program reads log entries from a file, classifies them into different categories, and stores the results in a structured format. The aim was to combine multiple concepts from the workshops into a single application.

## Learning from Workshops

### Workshop 7 – Comments, Libraries, JSON

In Workshop 7, I learned how to write clear comments and how to use external libraries in Python. I also learned how JSON works as a structured data format.

In this project:
- I used comments to explain the purpose of different parts of the code.
- I used the `json` library to save results into a JSON file instead of only printing them.
- I applied JSON structure to store data in a readable and reusable way.

---

### Workshop 8 – Regular Expressions, File I/O, Testing

In this workshop, I learned how to use regular expressions for pattern matching, how to read and write files, and how to test functions.

In this project:
- I used pattern matching to identify whether a line contains `INFO`, `WARNING`, or `ERROR`.
- I read input data from `logs.txt` and processed it line by line.
- I created output files such as `results.json`.
- I implemented a separate test file to verify that the program works correctly.

---

### Workshop 9 – Object-Oriented Programming

In Workshop 9, I learned how to create classes, use constructors, and organise code using object-oriented principles.

In this project:
- I created a `LogEntry` class to represent each log line.
- I used this class to determine the type of each log entry.
- This improved code structure and made the program more modular.

---

### Workshop 10 – Regex Improvement and Testing

In this workshop, I learned how to improve pattern matching and ensure reliability through testing.

In this project:
- I refined how log types are identified instead of relying only on simple checks.
- I used testing to confirm that the functions behave correctly.
- I focused on making the program more reliable and consistent.

---

## Design and Structure

The program was divided into separate files in order to improve clarity and maintainability.

- `main.py` controls the main execution flow  
- `models.py` contains the `LogEntry` class  
- `helpers.py` contains supporting functions  
- `test_log.py` is used for validation and testing  

This structure made the project easier to develop incrementally and reduced the risk of placing all logic in a single file.

## Conclusion

This project helped me combine multiple workshop topics into a single application. I was able to use regular expressions, file handling, JSON, testing, and object-oriented programming together. It also demonstrated the importance of structuring code clearly and verifying correctness through testing.