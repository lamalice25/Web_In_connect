from DDos_test import DDOS_test
from get_ip import get_ip
from recup_test import recup

print('\033[1;35;40m   *************')
print('  *             *')
print(' *               *')
print('\033[1;35;40m*  web in connect *\033[1;35;40m')  
print(' *               *')
print('  *             *')
print('   *************\033[0m')

print('=======================')

print('1.DDos test')
print('2.get ip test')
print('3. recup data test')

choice = input('Entrer votre choix : ')

if choice == "1":
    DDOS_test()

elif choice == "2":
    get_ip()

elif choice == "3":
    recup()