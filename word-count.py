count_dictionary = {}

def update_counts(count_dictionary, word):
    if word in count_dictionary:
        count_dictionary[word] = count_dictionary[word] + 1
    else:
        count_dictionary[word] = 1

text = input("Enter some text: ")
text = text.split()

for word_ in text:
    update_counts(count_dictionary, word_)

print(count_dictionary)