from info import name #type: ignore
from info import author #type: ignore
from info import maintainer #type: ignore
from info import version #type: ignore
from info import readme #type: ignore
from info import license #type: ignore
from info import help
import os #type: ignore
def many(): #type: ignore
    print("NAME: " + name) #type: ignore
    print("AUTHOR: " + author) #type: ignore
    print("MAINTAINER: " + maintainer) #type: ignore
    print("VERSION: " + version) #type: ignore
    print("README: when prompted run /r") #type: ignore
    print("LICENSE: when prompted run /l") #type: ignore
    while True:
        ask = input("press and run what? /")
        if ask == ("r"):
            print("README: ")
            os.system(readme)
        elif ask == ("l"):
            print("LICENSE: ")
            os.system(license)
            print("")
        elif ask == ("q"):
            exit()
        elif ask == ("h"):
            print(help)
        elif ask == ("c"):
            os.system("clear")
        elif ask == ("m"):
            os.system("python3 scrap/scrap.py")
        elif ask == (""):
            print("!!Query Empty!!")
        elif ask == (" "):
            print("!!Query Empty!!")
        elif ask == ("/"):
            print("ii-slashshell-ii")
        elif ask == ("!"):
            ter = input("/")
            os.system(ter)
        elif ask == ("hello"):
            print("Hello, World!")
        else:
            print(ask + " <-- !!Error Unknown Command!!")
def start(ver): #type: ignore
    print("scrap: " + ver) #type: ignore
    print("scrap: know") #type: ignore
    print("scrap: live") #type: ignore
start("1") #type: ignore
startopen = input("Press ENTER/RETURN to continue!") #type: ignore
if startopen == (""): #type: ignore
    many() #type: ignore
else: #type: ignore
    print("Error!") #type: ignore
