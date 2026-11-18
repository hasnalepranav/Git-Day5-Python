text = " Hello, Good Morning! "

print("Remove Spaces", text.strip()) #strips spaces from both endsd

print("Upper Case", text.upper())

print("Lower Case", text.lower())

text = text.strip() #Capitalize first letter of string
print("Capitalize First Letter", text.capitalize())

print(text.title()) #capitalize each word

print("Letter G Occurs", text.count("G"),"times in text") #count occurences of a string

print(text.replace("Hello", "Python Logic")) #replace a substring

print(text.startswith("  We")) #Starts if string starts or ends with certain substring
print(text.endswith("!  "))

print("Simple split", text.split()) #splits the strings on whitespace into a list of words

words = ["Python", "Is", "Fun"] #Define list of strings

print(" ".join(words)) #concatenates elements of an iterable using specified delimiter
