from posixpath import split
from unittest import result


sentence = "What is an air speen velocity of an unladen swallow"

result = { word: len(word) for word in sentence.split()}


print(result)