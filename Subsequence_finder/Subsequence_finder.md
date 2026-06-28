# Fast Subsequence Finder

## Overview
**Fast Subsequence Finder** is a highly efficient Python script designed to determine which words from a given list are valid subsequences of a target string. 

Instead of using a basic two-pointer approach for every single word—which can be slow for large datasets—this script optimizes the search by pre-computing character positions and utilizing binary search (`bisect`). This makes it exceptionally fast when checking multiple words against a single, long string.

## Features
* **Efficient Pre-computation:** Maps every character in the main string to a list of its indices, running in $O(N)$ time.
* **Binary Search Optimization:** Uses Python's built-in `bisect` module to quickly locate the next valid character index in $O(\log K)$ time, bypassing the need to linearly scan the string.
* **Performance Tracking:** Built-in execution timer using `time.perf_counter()` to measure the exact time taken to process the strings down to the microsecond.
* **Zero Dependencies:** Built entirely using Python's standard library. No external packages like `numpy` or `pandas` are required.

## How It Works
1. **Index Mapping:** The script first reads the main string and creates a dictionary (hash map) where each key is a character and the value is a list of all indices where that character appears.
2. **Binary Searching:** For each character in a test word, the script looks up its available indices in the dictionary. It then uses binary search (`bisect_right`) to find the smallest index that appears *after* the previously matched character. 
3. **Validation:** If all characters in the test word are found in the correct sequential order, it is flagged as a valid subsequence.

## Usage

### Prerequisites
* Python 3.x

### Getting Started
1. Clone or download the repository to your local machine.
2. Open `Subsequence_finder.py` in your preferred text editor or IDE.
3. **Set your variables:**
   * Modify the `s` variable to be your main target string.
   * Modify the `s2` variable (which can be a tuple or a list) to contain the words you want to check.

```python
# --- Configuration ---

# 1. Add your main string here:
s = 'dsahjpjauf'

# 2. Add the list/tuple of strings to check against 's' here:
s2 = ('ahjpjau', 'ja', 'ahbwzqqnuk', 'tnnlanowax')
