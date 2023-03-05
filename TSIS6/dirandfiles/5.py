color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('a.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('a.txt')
print(content.read())