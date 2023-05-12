input = input("Enter the sentence: ")
sentence = input.lower()

count = 0
vowels = ["a","e","i","o","u"]

for char in sentence:
    if char in vowels:
        count+=1

print("The vowel count is: ", count)