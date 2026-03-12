# Algorithmic problems in Python

This repository contains solutions to several **algorithmic problems** implemented in Python.

The tasks demonstrate different algorithmic techniques including:

- hash tables
- greedy algorithms
- dynamic programming
- combinatorics and string analysis

---

Each file contains:

- problem solution
- function implementation
- unit tests using `assert`

---

# Implemented Problems

## 1. Students in Exactly k Clubs

Given a list of clubs and their members, determine how many students belong to **exactly $k$ clubs**.

Example input:
```
2 robotics:1,2,3 chess:2,4,5 drama:1,2,6
```


The algorithm counts the occurrences of each student ID using a dictionary.

Time complexity:

$$
O(n)
$$

where $n$ is the total number of student IDs.

Implementation:
```
k_clubs(input_string)
```


---

# 2. Maximum Number of Non-Overlapping Events

Given a set of events with start and end times, determine the maximum number of events that can be scheduled without overlap.

Example:
```
pyramids:1-5 rome:2-4 renaissance:5-8 revolution:6-9
```


The solution uses a **greedy algorithm**:

1. sort events by finishing time
2. always choose the earliest finishing event.

Time complexity:

$$
O(n \log n)
$$

due to sorting.

Implementation:
```
max_events(input_string)
```


---

# 3. Magic Power (Dynamic Programming)

Determine the **minimum number of ingredients** needed to achieve a desired magic power.

Example:
```
11 1 5 6
```


The solution uses **dynamic programming** similar to the classic **coin change problem**.

Let:

- $P$ — desired power
- $a_i$ — power of ingredient $i$

DP relation:

$$
dp[j] = \min(dp[j], dp[j-a_i] + 1)
$$

Time complexity:

$$
O(P \times n)
$$

where:

- $P$ — target power
- $n$ — number of ingredients.

Implementation:
```
magic_power(input_string)
```


---

# 4. Palindromic Anagram Detection

A word can form a palindrome if **at most one character has odd frequency**.

Condition:

$$
\text{odd\_count} \le 1
$$

Example:
```
aab abc racecar hello
```

Result:
```
2
```


because:

- `aab → aba`
- `racecar → racecar`

Time complexity:

$$
O(n \cdot m)
$$

where:

- $n$ — number of words
- $m$ — average word length.

Implementation:

```
count_palindromic_anagrams(text)
```

---

# Purpose of the Project

This repository was created to practice:

- algorithm design
- Python problem solving
- greedy algorithms
- dynamic programming
- hash-based counting techniques.
