import os
import getpass
os.system("tput setaf 1")

print("\t\t\thii welcome to my TUI")

os.system("tput setaf 5")
print("\t\t\t---------------------")

Password=getpass.getpass("Enter your Password:")
apass="Prince"
if Password != apass:
	print("Auth Incorrect check the password")
	exit

print("where you would like to perform your job (local/Remote):",end="")
location=input()
print(location)

if location == "remote":
	remoteIP = input("Enter your Target IP:")

os.system("tput setaf 4")
while True:
	print(""" Chose
        Press1: To see date
	Press2: TO see Cal
	Press3: config web server
	Press4: Add new User
	Press5: To create a file
	Press6: To Check IP of system
	Press7: To Configure Docker
        Press8: To Create Own Python File
        Press9: To Create Own Terraform Code 
        Press10:To Create Terraform code
        Press11:Exit """)

	os.system("tput setaf 3")
	print("Enter your choice:",end="")
	ch=input()

	os.system("tput setaf 2")
	print(ch)

	if location=="local":
		if int(ch)==1 :
			os.system("date")
		elif int(ch)==2 :
			os.system("cal")
		elif int(ch)==3 :
			os.system("yum install webserver")
		elif int(ch)==4 :
			print("Give username here:",end="")
			UserAdd= input()
			os.system("useradd {}".format(UserAdd))
		elif int(ch)==5 :
			print("Give File name Here:",end="")
			Filename= input()
			os.system("mkdir {}".format(Filename))
		
		elif int(ch)==6:
			os.system("ifconfig")
                
		elif int(ch)==7:
                        os.system("yum install docker-ce --nobest")
		elif int(ch)==8:
                        print("Give your Python file name with .py ectension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))    
			
		elif int(ch)==9:
                        print("Give your file name with .tf extension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))
		elif int(ch)==10:
			while True:
				print("""  To Create a New Directory.
             2. To Open Text Editor
             3. To Delete the Directory
             4. To Open Firefox Browser
             5. To Create a New User
             6. To Check IP of System
             7. To Stop Firewall
             8. To Set SE Linux Permissive
             9. To Configure yum
            10. To Check Running Ports
            11. To Check Running Processes
            12. To Check PID of Process
            13. To Kill Process
            """)
			     os.system("tput setaf 3")
	             print("Enter your choice:",end="")
	             ch1=input()
				 os.system("tput setaf 2")
	             print(ch)
				  if ch == 1:
        dirname = input("Enter Name of directory:")
        os.system("mkdir {}".format(dirname))
    elif ch == 2:
        filename = input("Enter Name of File:")
        os.system("vim {}".format(filename))
    elif ch == 3:
        dirname = input("Enter Name of directory:")
        os.system("rmdir -f {}".format(dirname))
    elif ch == 4:
        os.system("firefox")
    elif ch == 5:
        username = input("Enter Username:")
        os.system("useradd {}".format(username))
    elif ch == 6:
        os.system("ifconfig")
    elif ch == 7:
        os.system("systemctl stop firewalld")
    elif ch == 8:
        os.system("setenforce 0")
   # elif ch == 9:
   #     os.system("cat > /etc/yum.repos.d/my_stable_repo >>
   #             [my_stable_repo]
   #             name = Stable Repo
   #             baseurl = 'https://myurl/$releasever/stable/Packages/'
   #             enabled = 1
   #             gpgcheck = 0
   #             EOF")
    elif ch == 10:
        os.system("netstat -tlnp")
    elif ch == 11:
        os.system("ps -aux")
    elif ch == 12:
        processname = input("Enter Process Name")
        os.system("ps -aux | grep -i {}".format(processname))
    elif ch == 13:
        pid = int(input("Enter Process ID/PID:"))
        os.system("kill {}".format(pid))

		elif int(ch)==11:
                        exit()
		else:
			print("Not responding")
	
	elif location=="remote":
		if int(ch)==1 :
			os.system("ssh {} date".format(remoteIP))
		elif int(ch)==2 :
			os.system("ssh {} cal".format(remoteIP))
		elif int(ch)==3 :
			os.system("ssh {} yum install webserver".format(remoteIP))
		elif int(ch)==4 :
			print("Give username here:",end="")
			UserAdd= input()
			os.system("ssh {} useradd {}".format(remoteIP,UserAdd))
		elif int(ch)==5 :
			print("Give File name Here:",end="")
			Filename= input()
			os.system("mkdir {}".format(Filename))	
		else:
			print("dont support")
	else:	
		print("Not location found")
	input("Enter the continue -> -> ->")
	os.system("clear")
os.system("tput setaf 6")
