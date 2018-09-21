'''The program extract the price starting at any dynamic position in Html page. The price is four characters long.
.Price-grabbing program extracts the four-character substring that follows the occurence of the “>$” characters.
Store the price substring in a variable called price.The program also keeps checking the website until the price of
the beans falls below $4.74'''

import urllib.request
import time
def set_beans_price():
    page=urllib.request.urlopen("https://dir.indiamart.com/impcat/coffee-beans.html")
    textfile=str(page.read())
    t1="Rs&nbsp"    
    where=textfile.find(t1)
    start_of_price=where+8
    end_of_price=start_of_price+3
    price=textfile[start_of_price:end_of_price]
    return float(price)


choice=0
coffee_beans=0.00
while choice!=3:
    print("1.To check Price")
    print("2.To inform at lower Price")
    print("3.To quit")
    choice=input("Enter your choice:")
    choice=int(choice)
    if int(choice)==1:
        coffee_beans=set_beans_price()
        print(coffee_beans)
    if int(choice)==2:
        coffee_beans=set_beans_price()
        while coffee_beans>137.0:
            time.sleep(40)
            coffee_beans=set_beans_price()
            print("Higher Prices")
        print("Time to buy at Low Prices")
print("Thank You for using the application")

'''PYTHON TOOLS:
* s[4] - access the 5th character of the variable “s",
which is a string
* s[6:12] - access a sub-string within the string “s" (up
to, but not including)
*s.find() method for searching strings
* s.upper() method for converting strings to
UPPERCASE
* float() converts strings to decimal point numbers
known as “floats"
* + addition operator
* > greater than operator
* urllib.request library for talking to the Web
* time library for working with dates/time'''

        

    
    
    
