validEmail = 'myEmail@me.com'
validPassword = '12324'
# -------------------------------

email = input('[?] Enter Your Email: ')
password = input('[?] Enter Your Password: ')

if (email == validEmail) and (password == validPassword):
    print('[+] Login Successfully!')
    print('Redirecting You in Few Moments..')
else:
    print('[-] Login Failed!')
    exit()

print('''
    
    >>>>> Welcome To My App <<<<
          Hope U Interested
    
    ''')


