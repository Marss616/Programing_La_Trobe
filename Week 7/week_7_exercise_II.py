# Jack Bell / Mars616 - 05 JAN 2024

sentence = input("Input please: ")
dont_count_set = {"a", "an", "the", "as", "by", "for", "in", "of", "on", "to"}

# Create the filtered sentence form the sentance input and the dont_count_set
filtered_sentence = ' '.join(word for word in sentence.split() if word.lower() not in dont_count_set)

count = len(filtered_sentence)
letters = ""

if letters in filtered_sentence != " ":
    print("this")
else:
    count = count + 1

print(count)