def solution(S):
    sentences = S.replace('!', '.').replace('?', '.').split('.')
    
    max_words = 0
    
    for sentence in sentences:
        words = [word for word in sentence.split() if any(c.isalpha() for c in word)]
        max_words = max(max_words, len(words))
    
    return max_words

# Test cases
print(solution("We test coders. Give us a try?"))
print(solution("Forget CVs..Save time . x x"))