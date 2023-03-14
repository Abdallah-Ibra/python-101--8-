
# # ? Open File 
# myfile = open('names.txt','r')

# # ! Operations
# # print(myfile.read())
# # ** read() --> str()
# # ** readline() --> str() [Fist Line in File]
# # ** readlines() --> list()
# # ** readable() --> bool()

# # data1 = myfile.read()
# # print(data1[:5])
# # data2 = myfile.readline()
# # print(data2.strip())

# # data3 = myfile.readlines()
# # print(type(data3))

# # for x in data3:
# #   print(f'Item1: {x.strip()}')

# # isReadable = myfile.readable()
# # print(isReadable)

# # ? Close File 
# myfile.close()





#! read() --> str
#! readline() --> str
#! readlines() --> list
#! readable() --> True|False

# myFile = open('(13) File Handling/names.txt','r')
# myFile = open('E:\\python\\python 101 (8)\\(13) File Handling\\names.txt','r')
# myFile = open('E:/python/python 101 (8)/(13) File Handling/names.txt','r') #? Full Path
# myFile = open('names.txt','r') #? Relative Path
# txt = myFile.read()
# print(txt[0])
# line = myFile.readline()
# print(line.strip())
# lines = myFile.readlines()
# print(lines[0].replace('\n',''))
# print(lines[-1].strip())
# print(type(lines))
# print(len(lines))
# print('[#] Getting All Data .. \n')
# for name in lines:
#     print(f'  [+] Name --> {name.strip().title()}')
#     print('-'*40)

# print('[?] Is This File Readable? {}'.format(myFile.readable()))

# myFile.close()



f = open('test.txt','w')
names = ['Ahmed','Essaa','Amir','Joudy','Yousef']
# f.write('Hello From Vision!\nHello From Vision!\nHello From Vision!\nHello From Vision!\nHello From Vision!\n')
# f.write('Hello From Vision!\n')
# f.write('Hello From Vision!\n')
# f.write('Hello From Vision!\n')

# f.writelines(names)
# for name in names:
#     print(name)

# for x in range(len(names)):
#     print(names[x])


for x,y in enumerate(names):
    print(f'[{x}]. {y}')

f.close()