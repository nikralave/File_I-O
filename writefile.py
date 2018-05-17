# f  = open('data.txt', 'a')
# f.write("Hello World\n")
# f.close()
#----------------------------------------------------
words = ["The", "quick", "brown", "fox"]

words_as_string = "\n".join(words)

f = open("newfile.txt", "w")



f.writelines(words_as_string)
f.close()
