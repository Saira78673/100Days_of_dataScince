# Q1: count Vowels . find how many vowels are in a string

text='programming'
count = 0
for ch in text.lower():
    if ch in 'aeiou':
        count +=1
        
# print(count)
# //////////////////////////////////////////////////////////
# # Q2: check whether a word is a palindrome 
# word = input('entere a number to check:')

# if word == word[::-1]:
#     # print('palindrome')
# else:
#     # print("not palindrome")

# Q3:count character 
text = 'banana'
print(text.count('a'))



