# ==================================================================
## Open File ##
# my_file = open("paragraph.txt","r")

## Operations on File ##
# read_file = my_file.read(30)
# print(type(read_file))
# print(read_file)
# input("[?] read more..")
# read_file = my_file.read()
# print(read_file)

# readline_file = my_file.readline(10)
# print(readline_file)

# readlines_file = my_file.readlines()
# print(readlines_file)

# readable_file = my_file.readable()
# print(readable_file)

## Close File ##
# my_file.close()

# ===================================================================

## Writting on File ##

# myFile = open('test.txt','w')
# myFile.write('Hello From VisionPlus!')
# x = myFile.writable()
# print(x)
# my_list = ['Ahmed\n','Abdallah\n','Ali\n']
# myFile.writelines(my_list)
# myFile.close()

# ===============================================

## Appending on File ##

# myFile = open('paragraph.txt','a')
# myFile.write('Successful Student\n')
# myFile.write('failed Student\n')
# myFile.close()

# ## Write and Read at The Same Time ##

# myFile  = open('test.txt','r+')
# v = myFile.read()
# print(v)
# myFile.write('Nothing!')
# myFile.close()
#==================================================================
# with open('test.txt','r') as myFile:
    # print(myFile.readlines())
    # myFile.close()


# myFile = open("credintals.txt","r")
# # print(myFile.readlines())
# lines = myFile.readlines()
# x = 1
# for line in lines:
#     # print(line.strip())
#     userpass = line.strip()
#     print(f"[{str(x).zfill(2)}] {userpass}")
#     # username = userpass.split(":")[0]
#     # password = userpass.split(":")[1]
#     username, password = userpass.split(":")
#     # print(f"\tUsername --> {username}")
#     # print(f"\tPassword --> {password}")
#     with open("new_output.txt","a") as n_o:
#         n_o.write(f"username: {username}\nPassword: {password}")
#         n_o.write("\n"+"-"*50+'\n')
#     x+=1
# myFile.close()
# ======================================


# with open("paragraph.txt","r") as ph:
#     lines = ph.readlines()
    # print(lines)
    # for l in lines:
        # print(l.strip())
        # if "|" in l:
        #     data = "[+] Found Data --> {}".format(l.strip())
        #     print(data)
        #     with open("new_output.txt","a") as output:
        #         output.write(data+"\n")
        # if l.startswith("user"):
        #     data = "[+] Found Data --> {}".format(l.strip())
        #     print(data)


# myData = open("mydata.csv","r") 
# n_data = myData.readlines()
# z = 0
# for i in n_data:
#     # print(i.split("\t"))
#     x = i.split("\t")[0]
#     y = i.split("\t")[1]
#     # (x+y)**2
#     result = (float(x)+float(y))**2
#     print("X{}: {}".format(z,x.strip()))
#     print(f"Y{z}: {y.strip()}")
#     print(f"Result: ({x.strip()}{z}+{y.strip()}{z})**2 = {result}\n")
#     z+=1
#     with open("new_output.csv","a") as op:
#         op.write(str(result)+"\n")
# myData.close()


# myFile = open('test.txt','r')
# valid_file = open('valid.txt','a')
# invalid_file = open('invalid.txt','a')

# userpass = myFile.readlines()
# userpass = myFile.readline()
# x = userpass.strip().split(':')
# username,password = x

# x = x.split(':')
# print(x)
# username = x[0]
# password = x[1]
# print(username)
# print(password)

# for i in userpass:
#    user,password = i.strip().split(':')
#    # print(f'[+] Username: {user}')
#    # print(f'[+] Password: {password}')
#    if user.startswith('user') and password.startswith('pass'):
#       print(f'[+] Valid Credintals: {user}|{password}')
#       valid_file.write(f'{user}|{password}\n')
#    else:
#       print('[-] Invalid Credintals: {user}|{password}')
#       invalid_file.write(f'{user}|{password}\n')
#    print('-'*50)
# myFile.close()
# valid_file.close()
# invalid_file.close()

# input('\n[!] Hit Any Key To Close..')



# with open('test.txt','r') as userpass:
#    user_pass = userpass.readlines()


# for i in user_pass:
#    user,password = i.strip().split(':')
#    # print(f'[+] Username: {user}')
#    # print(f'[+] Password: {password}')
#    if user.startswith('user') and password.startswith('pass'):
#       print(f'[+] Valid Credintals: {user}|{password}')
#       with open('valid.txt','a') as valid_file:
#          valid_file.write(f'{user}|{password}\n')
#    else:
#       print('[-] Invalid Credintals: {user}|{password}')
#       with open('invalid.txt','a') as invalid_file:
#          invalid_file.write(f'{user}|{password}\n')
#    print('-'*50)

# input('[?] Hit Any key To close..')





myFile = open(r'test.txt')
print(myFile.read())
myFile.close()