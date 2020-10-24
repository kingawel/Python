source = open('my_text2.txt','r') 
#original text
#ziemia sie kreci oraz nigdy nie przestanie.
#dlaczego tak jest oraz jak dlugo.
replace_dictionary = {"oraz":"i", "nigdy":"prawie nigdy", "dlaczego":"czemu", "i":"oraz"}
new_list = []
for line in source:
    for word in replace_dictionary:
        if word in line:
            line = line.replace(word,replace_dictionary[word])
    new_list.append(line) #list used to keep text from file with removed words
source.close()
source = open('my_text2.txt','w')
for line in new_list:
    source.write(line)
source.close()