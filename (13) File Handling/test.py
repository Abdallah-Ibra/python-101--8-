
# ? Open File 
myfile = open('names.txt','r')

# ! Operations
# print(myfile.read())
# ** read() --> str()
# ** readline() --> str() [Fist Line in File]
# ** readlines() --> list()
# ** readable() --> bool()

# data1 = myfile.read()
# print(data1[:5])
# data2 = myfile.readline()
# print(data2.strip())

# data3 = myfile.readlines()
# print(type(data3))

# for x in data3:
#   print(f'Item1: {x.strip()}')

# isReadable = myfile.readable()
# print(isReadable)

# ? Close File 
myfile.close()