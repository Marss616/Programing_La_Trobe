# Jack Bell / Mars616 - 05 JAN 2024

sentence = input("Input please: ")
dont_count_set = {"a", "an", "the", "as", "by", "for", "in", "of", "on", "to"}

filtered_words = set(
    word.lower() 
    for word in sentence.split() 
    if word.lower() not in dont_count_set
)
#Count the number of words in the filtered list
count = len(filtered_words)

print(count)
