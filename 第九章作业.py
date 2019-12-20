# a = abs(10) + abs(-10)
# print(a)
# b = abs(-10) + -10 
# print(b)


# abc = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
# print(dir(abc))
# help(abc.split)
# message = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
# words = message.split()
# for x in range(0, len(words)):
#     print(words[x])
    

f = open('1.txt')
s = f.read()
f.close()
f = open('2.txt', 'w')
f.write(s)
f.close()
import shutil
shutil.copy('1.txt', '2.txt')