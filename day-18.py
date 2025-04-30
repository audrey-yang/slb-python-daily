"""
Errata on Data

Difficulty: Hard

What might happen when you don't close a file in a Python program and open it after the code completes its execution?

Options:
- Data inconsistency
- File Descriptors limit reached
- File not found
X All of the above
"""

if __name__ == "__main__":
    print("Solution: All of the above")

"""
- Data inconsistency
    Without closing the file, it is not guaranteed that all the data will be written to disk.

- File Descriptors limit reached
    If we don't call `close` on a file, the file descriptor may not be released, which may lead to us hitting the limit for open file descriptions.

- File not found
    As with data inconsistency, it is not guaranteed that the file is written to disk. Therefore, it may not have been written at all.
"""
