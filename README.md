
### How to Use the Program

1. **Save the Code**: Copy the code above into a Python file (e.g., `text_analysis.py`).
2. **Prepare a Text File**: Create or use an existing text file (e.g., `sample.txt`) that you want to analyze.
3. **Run the Program**: Execute the program using Python. You can do this from the command line:

   ```bash
   python text_analysis.py
   ```

### Explanation of Key Components

- **Imports**: The program uses `re` for regular expression operations and `Counter` from the `collections` module for counting word frequencies.
- **File Handling**: It opens the specified text file and reads it line by line.
- **Counting Logic**:
  - Lines are counted directly.
  - Characters are counted using `len(line)`.
  - Words are extracted using a regular expression that matches word characters.
- **Word Frequency**: The `Counter` object updates with each found word, allowing easy retrieval of the most common words.
- **Output**: Results are printed in a structured format, including total counts and a list of the most frequent words.
