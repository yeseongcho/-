file = open ("./emma.txt", "r")
import string

line = file.read()
word = line.strip(string.punctuation+string.whitespace)

word1 = word.lower()
word2 = word1.split()

x= word2[0]
print (x)

print("-----------------")

for i in range(10):
    print(word2[i])
