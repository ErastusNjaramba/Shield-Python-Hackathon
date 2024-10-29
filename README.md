
# Algorithm Tasks: Implementation in Python

This repository includes implementations of various searching, string manipulation, and sorting algorithms in Python.



## Getting Started

To use this repository, clone it to your local environment:

```bash
git clone https://github.com/ErastusNjaramba/Shield-Python-Hackathon.git
cd Shield-Python-Hackathon
```

## Prerequisites

- Python 3.x
- Basic knowledge of algorithms and data structures

## Project Structure

The project is organized into modules, each containing specific algorithms based on the task. 

algorithm-tasks/
│
├── searching/
│   ├── ternary_search.py
│   └── rotated_array_search.py
│
├── string_manipulation/
│   ├── longest_substring.py
│   └── regex_match.py
│
├── sorting/
│   ├── custom_sort.py
│   └── kth_largest.py
│
└── README.md

---

## Algorithm Descriptions and Usage

### 1. Searching Algorithms

#### Ternary Search
**File**: `searching/ternarySearch.py`

**Description**: Implements the Ternary Search algorithm, which divides the array into three parts and recursively searches for the target element in a sorted array.


#### Search in Rotated Sorted Array
**File**: `searching/rotatedSortedArray.py`

**Description**: An algorithm to find a target value in an array sorted in ascending order but rotated at an unknown pivot point.



### 2. Advanced String Manipulation

#### Longest Substring Without Repeating Characters
**File**: `string_manipulation/longestSubstring.py`

**Description**: This function identifies the longest substring in a given string that contains no repeating characters and returns its length.

#### Regular Expression Matching
**File**: `string_manipulation/regExpMatching.py`

**Description**: Implements a basic regular expression matcher with support for `.` (matches any single character) and `*` (matches zero or more of the preceding character).



### 3. Sorting Algorithms

#### Custom Sort
**File**: `sortingAlgorithms/customSort.py`

**Description**: Sorts a list of dictionaries by a specified key, allowing for custom sorting logic based on various dictionary keys.

#### Kth Largest Element
**File**: `sortingAlgorithms/kthLargestElement.py`

**Description**: Finds the **Kth** largest element in an unsorted list, suitable for scenarios where quick access to the Kth largest element is needed.

