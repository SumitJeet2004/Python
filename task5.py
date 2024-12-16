import re
from collections import defaultdict
import os

def count_words(filename):
    word_counts = defaultdict(int)

    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    try:
        # Open and read the file
        with open(filename, 'r') as file:
            print(f"Reading file: {filename}")
            for line in file:
                print(f"Processing line: {line.strip()}")
                # Remove punctuation and convert to lowercase
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_counts[word] += 1

        if not word_counts:
            print("No words found in the file.")
        else:
            # Sort the words alphabetically and display the counts
            print("Word counts:")
            for word in sorted(word_counts):
                print(f'{word}: {word_counts[word]}')
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the correct path to your text file
file_path = 'C:/Users/sumit/OneDrive/Desktop/intern works/level 2/sample.txt'
count_words(file_path)
