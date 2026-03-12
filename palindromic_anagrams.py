"""Task 4"""

def count_palindromic_anagrams(text: str) -> int:
    """Count how many words in the given text can be rearranged to form a palindrome.

    A word can be rearranged to form a palindrome if at most one character has an odd frequency.

    Args:
        text (str): A string containing words separated by spaces."""

    counter = 0

    for word in text.split():
        char_counter = {}
        for char in word:
            char_counter[char] = char_counter.get(char, 0) + 1

        odd_count = sum(1 for count in char_counter.values() if count % 2 != 0)
        if odd_count <= 1:
            counter += 1
    return counter

def test_example_from_statement():
    assert count_palindromic_anagrams("aab abc racecar hello") == 2


def test_single_palindrome_word():
    assert count_palindromic_anagrams("civic") == 1
    assert count_palindromic_anagrams("racecar") == 1


def test_single_non_palindromic_but_anagrammable():
    # "aabb" -> "abba"
    assert count_palindromic_anagrams("aabb") == 1
    # "aab" -> "aba"
    assert count_palindromic_anagrams("aab") == 1


def test_single_impossible_word():
    # 3 різні символи з частотою 1 -> 3 непарні
    assert count_palindromic_anagrams("abc") == 0
    # "hello" -> h:1, e:1, l:2, o:1 -> 3 непарні
    assert count_palindromic_anagrams("hello") == 0


def test_multiple_words_mix():
    # "aa" (✓), "ab" (✗), "aabb" (✓), "abc" (✗) -> 2
    assert count_palindromic_anagrams("aa ab aabb abc") == 2


def test_all_words_ok():
    # всі можна зробити паліндромами:
    # "aa", "bbb", "aabb", "a" -> 4
    assert count_palindromic_anagrams("aa bbb aabb a") == 4


def test_no_words():
    # Порожній рядок — 0 слів, 0 паліндромів
    assert count_palindromic_anagrams("") == 0


def test_words_with_repeats_of_same_word():
    # "aab" (✓), "aab" (✓), "abc" (✗) -> 2
    assert count_palindromic_anagrams("aab aab abc") == 2

if __name__ == "__main__":
    test_example_from_statement()
    test_single_palindrome_word()
    test_single_non_palindromic_but_anagrammable()
    test_single_impossible_word()
    test_multiple_words_mix()
    test_all_words_ok()
    test_no_words()
    test_words_with_repeats_of_same_word()
    print("All tests passed.")
