file_handler=open("transaction.txt","a")
Menu={}
Menu['Latte']='130.00'
Menu['Tea']='165.62'
Menu['Cappicuno']='195.8'
Menu['Chocolate']='156.62'
running=True
Credit_card=0

while running:
    option=1
    item=""
    print("Menu:") #Dynamic Menu
    for each_item in Menu.keys():
        option
        print("%d.%s"%(option,each_item))
        option= option+1
    print("%d. To quit"%(option))
    running=False

    
    ch=input("Enter your choice by name in Menu\n")
    for each_item in Menu.keys():
        if ch==each_item:
            Credit_card=input("Enter your Credit card Details")
            file_handler.write("%16d,%s,%s \n"%(int(Credit_card),Menu[each_item],each_item))
            file_handler.close()
print("Thanks For Coming")
