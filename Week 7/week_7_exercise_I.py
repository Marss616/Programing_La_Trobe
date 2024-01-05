# Jack Bell / Mars616 - 05 JAN 2024

sentence = input("Input please: ")
dont_count_set = {"a", "an", "the", "as", "by", "for", "in", "of", "on", "to"}

# Split the sentence into words
words = sentence.split()

# Create a new list for words not in the dont_count_set
filtered_words = [word for word in words if word.lower() not in dont_count_set]

# Join the filtered words back into a sentence
filtered_sentence = ' '.join(filtered_words)

print(filtered_sentence)
