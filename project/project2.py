from colorama import Fore,init
import sys,time,os
init(convert=True)

# clear = lambda : os.system('cls')
def clear():
  try:
    os.system('cls')
  except:
    os.system('clear')

fruits = ['Tomato','Apple','Orange','Banana']
vegetables = ['Potato','Cucumber','Peper','Carrots']


banner = Fore.MAGENTA+'''
    ██╗   ██╗██╗███████╗██╗ ██████╗ ███╗   ██╗    ███████╗████████╗ ██████╗ ██████╗ ███████╗
    ██║   ██║██║██╔════╝██║██╔═══██╗████╗  ██║    ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
    ██║   ██║██║███████╗██║██║   ██║██╔██╗ ██║    ███████╗   ██║   ██║   ██║██████╔╝█████╗  
    ╚██╗ ██╔╝██║╚════██║██║██║   ██║██║╚██╗██║    ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
     ╚████╔╝ ██║███████║██║╚██████╔╝██║ ╚████║    ███████║   ██║   ╚██████╔╝██║  ██║███████╗
      ╚═══╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝                                                                                    
'''+Fore.RESET


while True:
  
  print(banner)
  print(Fore.LIGHTYELLOW_EX+'''
    1. Show All Products
    2. Add New Product
    3. Update/Edit on category/Product
    4. Delete Product
    5. Exit
  '''+Fore.GREEN)

  ask = int(input('[?] Choose An Option: '))
  print(Fore.RESET)
  if ask == 1:
    print(Fore.RED+'\n[#] Vegetables: '+Fore.CYAN)
    for y,i in enumerate(vegetables):
      print(f'   [{y+1}] {i}')

    print(Fore.RED+'\n[#] Fruits: '+Fore.CYAN)
    for y,i in enumerate(fruits):
      print(f'   [{y+1}] {i}')
  elif ask == 2:
    print(Fore.BLUE)
    newProduct = input('[?] Enter a new product: ').strip()
    catType = int(input('[?] Which Category [1.Fruits 2. Vegetables]: '))
    print(Fore.GREEN)
    if catType == 1:
      fruits.append(newProduct)
      print(f'[+] "{newProduct}" Added Successfully To "Fruits"')
    elif ask == 2:
      vegetables.append(newProduct)
      print(f'[+] "{newProduct}" Added Successfully To "Vegetables"')
    else:
      print(Fore.RED+'[!] Invalid Category!')
    print(Fore.RESET)
  elif ask == 3:
    # print('Update/Edit on category/Product Page!')
    print(Fore.CYAN)
    oldProduct = input('[?] Enter a old product: ').strip()
    newProduct = input('[?] Enter a new product: ').strip()
    catType = int(input('[?] Which Category [1.Fruits 2. Vegetables]: '))
    cat = fruits if catType == 1 else vegetables
    NewProductIndex = cat.index(oldProduct)
    cat[NewProductIndex] = newProduct
    print(Fore.GREEN+f'[+] "{oldProduct}" Updated Successfully To "{newProduct}"!'+Fore.RESET)
  elif ask == 4:
    # print('Delete Product Page!')
    product = input('[?] Enter The product: ').strip()
    catType = int(input('[?] Which Category [1.Fruits 2. Vegetables]: '))
    cat = fruits if catType == 1 else vegetables
    deleteProduct = cat.index(product)
    isDeleted = cat.pop(deleteProduct)
    print(Fore.RED+f'[-] "{isDeleted}" Deleted Successfully!'+Fore.RESET)
  elif ask == 5:
    print(Fore.RED+'[!] See You Again ^_0'+Fore.RESET)
    time.sleep(2)
    sys.exit()
  else:
    print(Fore.RED+'[!] Invalid Input!'+Fore.RESET)
  
  input(Fore.LIGHTWHITE_EX+'[?] Hit Enter To Continue ..')
  time.sleep(0.5)
  clear()
