"""
Create a Python program that analyzes text files in a given directory and reports
the top 10 words by frequency across all files.
"""

import os
from collections import Counter

def analyze_word_frequency(directory):
    word_counts = Counter()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                for line in file:
                    words = line.lower().split()
                    word_counts.update(words)
    return word_counts.most_common(10)

# Example usage
if __name__ == "__main__":
    print("Code Generation[2] Word Frequency Analyzer")

    directory = 'data/frequency'
    top_words = analyze_word_frequency(directory)
    for word, count in top_words:
        print(f"{word}: {count}")
