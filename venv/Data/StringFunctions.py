sentence = "London is the capital of Great Britain."
print(sentence)
sentence = sentence.lower()
print(sentence)
sentence.upper()
print(sentence)
sentence = sentence.replace("a", "x", 2)
print(sentence)
sentence.capitalize()
print(sentence)
sentence1 = "Help! Help! I’m being repressed!"
print((sentence1.strip(',.!?),').replace('!','')).lower())