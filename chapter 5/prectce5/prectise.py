words = {
    "Billi":"cat",
    "Khiladi":"player",
    "Ghar":"home",
}
word=input("Enter a word: ")
print(words[word])

s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s), s)

user_input1 = int(input("Enter a number: "))
user_input2 = int(input("Enter a number: "))
user_input3 = int(input("Enter a number: "))
user_input4 = int(input("Enter a number: "))
user_input5 = int(input("Enter a number: "))
procesed_set = set()
procesed_set.add(user_input1)
procesed_set.add(user_input2)
procesed_set.add(user_input3)
procesed_set.add(user_input4)
procesed_set.add(user_input5)
print(procesed_set)