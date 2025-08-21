vowel=['a','e','o','i','u']
word='programming'
count=0
for character in word:
    if character not in vowel:
        count +=1
        print(count)