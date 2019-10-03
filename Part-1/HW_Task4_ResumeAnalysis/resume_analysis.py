# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = os.path.join("Resources", "resume.md")

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)

# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)

# Using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")

# Clean Punctuation
_word_count = dict()
clean_list = []
for word in word_count:
    if word not in punctuation:
        _word_count[word] = word_count[word]
# Hint: consider using a list comprehension %% not used

# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
for word in stop_words:
    del _word_count[word]

# Sort words by count and print the top 10
sorted_words = []
for word in _word_count:
    for j in range(len(sorted_words)):
        if _word_count[word] > _word_count[sorted_words[j]]:
            sorted_words.insert(j, word)
            break
    if _word_count[word] not in sorted_words:
        sorted_words.append(word)

# Remove punctuations within the words
for word in sorted_words:
    word = word.split(',')[0].split('.')[0]

top10 = sorted_words[:10] 
print(top10)