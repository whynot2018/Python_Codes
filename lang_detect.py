#
#   PyThon Learning  @Faymaz
#       @programirez
#
# pip install langdetect
from langdetect import detect

#talking input from user
text = input("Enter any text in any language: ")

#printing output
print(detect(text))
