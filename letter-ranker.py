from collections import Counter

def sort_letters_by_frequency(letters):
    # Count the frequency of each letter
    letter_counts = Counter(letters)
    
    # Sort the letters by frequency (highest first)
    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)
    
    # Extract the sorted letters
    sorted_letters_only = [letter for letter, count in sorted_letters]
    
    return sorted_letters_only

file = input('what is the file name: ')

# Example usage
with open(file, 'r', encoding='utf-8') as r:
    letters = r.read()  # Call the read() method to get the file content

sorted_letters = sort_letters_by_frequency(letters)
print(sorted_letters)
