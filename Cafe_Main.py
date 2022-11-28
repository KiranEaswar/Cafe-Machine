import pickle
import sys
import time
from colorama import Fore,Back,init,Style
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./45)
def rupee_update(yenni):
    a=open('moni.txt')
    b=a.read()
    c=int(b)+yenni
    a.close()
    a=open('moni.txt','w')
    a.write(str(c))
    a.close()
def menu_show():
    menu=open('Menu_A_C.dat','rb')
    count=0
    a=pickle.load(menu)
    print(Fore.BLUE)
    print('𝓒𝓸𝓯𝓯𝓮𝓮')
    print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|','𝒩𝑜.','𝐼𝓉𝑒𝓂','𝒮𝓂𝒶𝓁𝓁','𝐿𝒶𝓇𝑔𝑒','|'))
    for i in range(3):
        count+=1
        print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|',str(count),a['Coffee'][i][0],'₹'+str(a['Coffee'][i][1]),'₹'+str(a['Coffee'][i][2]),'|'))
    print()
    print('𝓣𝓮𝓪')
    print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|','𝒩𝑜.','𝐼𝓉𝑒𝓂','𝒮𝓂𝒶𝓁𝓁','𝐿𝒶𝓇𝑔𝑒','|'))
    for i in range(3):
        count+=1
        print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|',str(count),a['Tea'][i][0],'₹'+str(a['Tea'][i][1]),'₹'+str(a['Tea'][i][2]),'|'))
    print()
    print('𝓗𝓸𝓽 𝓒𝓱𝓸𝓬𝓸')
    print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|','𝒩𝑜.','𝐼𝓉𝑒𝓂','𝒮𝓂𝒶𝓁𝓁','𝐿𝒶𝓇𝑔𝑒','|'))
    for i in range(2):
        count+=1
        print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|',str(count),a['Hot Choco'][i][0],'₹'+str(a['Hot Choco'][i][1]),'₹'+str(a['Hot Choco'][i][2]),'|'))
    print()
    print('𝓘𝓬𝓮𝓭 𝓑𝓮𝓿𝓮𝓻𝓪𝓰𝓮𝓼')
    print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|','𝒩𝑜.','𝐼𝓉𝑒𝓂','𝒮𝓂𝒶𝓁𝓁','𝐿𝒶𝓇𝑔𝑒','|'))
    for i in range(4):
        count+=1
        print('{:1}{:5}{:25}{:7}{:7}{:1}'.format('|',str(count),a['Iced Beverages'][i][0],'₹'+str(a['Iced Beverages'][i][1]),'₹'+str(a['Iced Beverages'][i][2]),'|'))
    print(Fore.RESET)
    menu.close()
def orderplace():
    b=open('b.dat','wb')
    v=input(Fore.YELLOW+'Set Order?(y/n)\n'+Fore.RESET)
    v.lower()
    ticket=[]
    if v=='n':
        b.close()
        print('ok')
    elif v=='sinchangreat' or v=='gengai01':
        print('How the hell do you know this?')
    elif v == 'y' or v == 'Y':
        menu_show()
        print(Back.YELLOW+'Please place your order'+Back.RESET)
        order = orderwrite()
        ticket.append(order)
        while True:
            order_again=input(Fore.YELLOW+'Place another order?(y/n)')
            order_again.lower()
            if order_again=='y':
                order = orderwrite()
                ticket.append(order)
            else:
                break
        print('Do you want to confirm the order?(y/n)')
        can=input()
        if can=='y'or can=='Y':
            print('Thank you for ordering, collect your order at the food counter')
            pickle.dump(ticket, b)
            b.close()
        else:
            print('OK, order cancelled')
            b.close()
            b=open('b.dat','wb')
            b.close()
def orderwrite():
    bruh=open('Menu_A_C.dat','rb')
    d=pickle.load(bruh)
    orderboi=[]
    print('Enter number of the food item you want to order:')
    a=int(input('->:'))
    while True:
        if a>=1 and a<=12:
            break
        else:
           print('Wrong Input')
    while True:
        size=input('Enter size(s-small,l-large)\n->:')
        size.lower()
        if size=='s' or size=='l':
            break
        else:
            print('Wrong Input')
    while True:
        x=int(input('Enter quantity\n->:'))
        if x>=1:
            print('Item Ordered') 
            if a>=1 and a<=3:
                if a==1:
                    n=0
                elif a==2:
                    n=1
                elif a==3:
                    n=2
                orderitem=d['Coffee'][n][0]
                if size=='s':
                    ordercost=int(d['Coffee'][n][1])
                else:
                    ordercost=int(d['Coffee'][n][2])
                orderq=x
                ordertotal=orderq*ordercost
                orderboi=[orderitem,str(ordercost),str(orderq),ordertotal]
                bruh.close()
                return orderboi
            elif a>=4 and a<=6:
                if a==4:
                    n=0
                elif a==5:
                    n=1
                elif a==6:
                    n=2
                orderitem=d['Tea'][n][0]
                if size=='s':
                    ordercost=int(d['Tea'][n][1])
                else:
                    ordercost=int(d['Tea'][n][2])
                orderq=x
                ordertotal=orderq*ordercost
                orderboi=[orderitem,str(ordercost),str(orderq),ordertotal]
                bruh.close()
                return orderboi
            elif a==7 or a==8:
                if a==7:
                    n=0
                elif a==8:
                    n=1
                orderitem=d['Hot Choco'][n][0]
                if size=='s':
                    ordercost=int(d['Hot Choco'][n][1])
                else:
                    ordercost=int(d['Hot Choco'][n][2])
                orderq=x
                ordertotal=orderq*ordercost
                orderboi=[orderitem,str(ordercost),str(orderq),ordertotal]
                bruh.close()
                return orderboi
            else:
                if a==9:
                    n=0
                elif a==10:
                    n=1
                elif a==11:
                    n=2
                elif a==12:
                    n=3
                orderitem=d['Iced Beverages'][n][0]
                if size=='s':
                    ordercost=int(d['Iced Beverages'][n][1])
                else:
                    ordercost=int(d['Iced Beverages'][n][2])
                orderq=x
                ordertotal=orderq*ordercost
                orderboi=[orderitem,ordercost,orderq,ordertotal]
                bruh.close()
                return orderboi
        else:
            print('Wrong Input')
def bill():
    a=open('b.dat','rb')
    c=open('moni.txt','r')
    print('                     ASTEROID CAFE')
    print('                Beverages From The Void')
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('{:5}{:25}{:10}{:10}{:1}{:5}'.format('S.no','Item','Cost','Quantity','|','Total'))
    count=0
    totaltotal=0
    b=pickle.load(a)
    for i in b:
        count+=1
        print('{:5}{:25}{:10}{:10}{:1}{:5}'.format(str(count),i[0],i[1],i[2],'|',str(i[3])))
        totaltotal+=i[3]
    rupee_update(totaltotal)
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
    print('{:5}{:25}{:10}{:10}{:1}{:5}'.format('','Total','','','|','₹'+ str(totaltotal)))
    print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
slowprint(Fore.GREEN+'''
█▀▀█ █▀▀ ▀▀█▀▀ █▀▀ █▀▀█ █▀▀█  ▀  █▀▀▄ 　 █▀▀ █▀▀█ █▀▀ █▀▀ 
█▄▄█ ▀▀█   █   █▀▀ █▄▄▀ █  █ ▀█▀ █  █ 　 █   █▄▄█ █▀▀ █▀▀ 
▀  ▀ ▀▀▀   ▀   ▀▀▀ ▀ ▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀  　 ▀▀▀ ▀  ▀ ▀   ▀▀▀''')
print('Our signature brew, for a taste of the Void')
print()
print()
print(Fore.WHITE+'''                                                 

                           *     .--.
                                / /  `
               +               | |
                      '         \ \__,
                  *          +   '--'  *
                      +   /\\
         +              .'  '.   *
                *      /======\      +
                      ;:.  _   ;
                      |:. (_)  |
                      |:.  _   |
            +         |:. (_)  |          *
                      ;:.      ;
                    .' \\:.    / `.
                   / .-'':._.'`-. \\       
                   |/    /||\    \|''')
print('''                  ..--"""````"""--..
           .-'``                    ``'-.
         -'                                '-''')
print(Style.RESET_ALL)
while True:
    print('''
           MENU
    1) View the Menu
    2) Place an Order
    3) View Bill
    4) See total cash in the Machine
    5) Withdraw an amount in the Register Machine
    6) Turn off the Register Machine''')
    choice=int(input('->:'))
    if choice==1:
        menu_show()
    elif choice==2:
        orderplace()
    elif choice==3:
        bill()
    elif choice==4:
        money=open('moni.txt')
        print('The total cash in the register is:₹',money.read())
        money.close()
    elif choice==5:
        money=open('moni.txt')
        x=int(money.read())
        money.seek(0)
        print('The total cash in the register is:₹',money.read())
        moneygone=int(input('Enter amount to withdraw   ->:'))
        if moneygone>x:
            print('The register does not contain the amount of money you have entered')
        else:
            x-=moneygone
            money.close()
            money=open('moni.txt','w')
            money.write(str(x))
            money.close()
            print('The money has been removed from the register')
    elif choice==6:
        slowprint('Shutting down machine . . . ')
        time.sleep(5)
        print('【Ｂｙｐａｓｓ　Ｓｐａｃｅ】™')
        print('A project by:')
        slowprint('Kiran E')
        slowprint('Sinchan B Rai')
        break
    else:
        print('You have entered an invalid input. Please enter again!')