letter_scores = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def calculate_score(word):
    word = word.upper()
    score = sum(letter_scores[letter] for letter in word if letter in letter_scores)
    return score


with open('ScrabbleWords.txt', 'r') as file:
    five_letter_words = [line.strip() for line in file.readlines()]

total_score = 0
total_words = len(five_letter_words)

for word in five_letter_words:
    total_score += calculate_score(word)

average_score = total_score / total_words

print(f"total words is : {total_words}")
print(f"total base score: {total_score}")
print(f"Average base score is: {average_score: 2f}")

