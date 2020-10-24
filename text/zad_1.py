source = open('my_text.txt','r') 
#original text
#Ziemia sie kreci i nigdy nie przestanie.
#Dlaczego tak jest i jak dlugo.
delete_list = [' sie ', ' nigdy ', ' i ', " oraz ", " nigdy ", " dlaczego "]
new_list = []
for line in source:
    for word in delete_list:
        if word in line:
            line = line.replace(word," ")
    new_list.append(line) #list used to keep text from file with removed words
source.close()
source = open('my_text.txt','w')
for line in new_list:
    source.write(line)
source.close()