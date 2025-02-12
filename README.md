# Longest Sentence Finder

## Description
This Python function finds the sentence containing the largest number of words in a given text. The text is split into sentences using `.`, `?`, and `!` as delimiters, and then each sentence is analyzed to count the number of words it contains.

## Function Definition
```python
def solution(S):
    # Split the text into sentences using '.', '?', '!' as delimiters
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    
    max_words = 0
    
    for sentence in sentences:
        # Split the sentence into words using spaces and count valid words
        words = [word for word in sentence.split() if any(c.isalpha() for c in word)]
        max_words = max(max_words, len(words))
    
    return max_words
```

## Example Usage
```python
print(solution("We test coders. Give us a try?"))  # Output: 4
print(solution("Forget CVs..Save time . x x"))  # Output: 2
```

## Assumptions
- The input string `S` consists only of letters (a-z, A-Z), spaces, dots (`.`), question marks (`?`), and exclamation marks (`!`).
- The length of `S` is between `1` and `100` characters.
- A word must contain at least one letter to be considered valid.

## Constraints
- No external libraries are used for text processing.
- Performance is not the primary concern, but correctness is ensured.

# longest-sentence-finder
