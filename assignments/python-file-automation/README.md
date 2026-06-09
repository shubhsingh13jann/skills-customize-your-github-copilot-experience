# 📘 Assignment: Python File Automation

## 🎯 Objective

Learn how to read from and write to files in Python while building a simple automation script that processes text data and saves a report.

## 📝 Tasks

### 🛠️ Read and Summarize Text Files

#### Description
Write a function named `summarize_file()` that reads a text file and returns a summary of its contents.

#### Requirements
Completed program should:

- Open a text file using a file path.
- Count the number of lines, words, and characters in the file.
- Return a dictionary with keys `lines`, `words`, and `characters`.
- Use `sample_notes.txt` as the sample input file.

#### Example

```python
summary = summarize_file("assignments/python-file-automation/sample_notes.txt")
print(summary)
# {'lines': 5, 'words': 11, 'characters': 59}
```

### 🛠️ Create a Clean Copy of the File

#### Description
Write a function named `copy_clean_file()` that reads a source text file and writes a cleaned version to a new file.

#### Requirements
Completed program should:

- Remove any empty lines from the input file.
- Preserve the original line order.
- Write the cleaned text to a new output file.
- Return the path to the cleaned file or print a success message.

#### Example

```python
clean_path = copy_clean_file(
    "assignments/python-file-automation/sample_notes.txt",
    "assignments/python-file-automation/clean_notes.txt"
)
print(clean_path)
# assignments/python-file-automation/clean_notes.txt
```

### 🛠️ Generate a Report File

#### Description
Write a function named `save_report()` that saves a summary report to a text file.

#### Requirements
Completed program should:

- Accept a summary dictionary containing file statistics.
- Write each statistic to the report file on its own line.
- Include a clear title at the top of the report.
- Use the report file name `report.txt`.

#### Example

```python
report = {
    "lines": 5,
    "words": 11,
    "characters": 59
}
save_report(report, "assignments/python-file-automation/report.txt")
```
