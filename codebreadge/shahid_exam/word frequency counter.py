words = []
while True:
    word = input("Enter a word (or 'done'): ")
    if word == "done":
        break
    words.append(word)

search_word = input("Enter word to search: ")
count = 0
index = 0

while index < len(words):
    if words[index] == search_word:
        count += 1
    index +=1
print(f"{search_word} appears {count} times")