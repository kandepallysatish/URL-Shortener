import pyshorteners  # MODULE USED

link = input("enter your link: ")  # ENTER YOUR LINK THAT YOU WANT TO SHORT
result = pyshorteners.Shortener().tinyurl.short(link)  # METHOD TO SHORT LINK
print(result)