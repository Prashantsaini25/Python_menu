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
	Press4: AWS (Menu)
	Press5: Basic Linux (Menu)
	Press6: To Check IP of system
	Press7: To Configure Docker
        Press8: To Create Own Python File
        Press9: To Create Own Terraform Code 
        Press10:Hadoop (Menu)
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
			while True:
				print("""
			Press1: Configure AWS
			Press2: Create a Key Pair Own AWS
			Press3: Create a Security Group AWS
			Press4: Launch AWS Instance
			Press5: Create new Volume """)
			
				os.system("tput setaf 3")
				print("Enter Your Choice:",end="")
				ch=input()
				os.system("tput setaf 2")
				print(ch)
				if int(ch)== 1:
					os.system("aws configure")
				elif int(ch) == 2:
					keyname = input("Enter Key Name:")
					os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
				elif int(ch)== 3:
					SGroupName = input("Enter Security Groupname:")
					vpcid = input("Enter VPC ID:")
					os.system('aws ec2 create-security-group --description "security group" --group-name "{}" --vpc-id {}'.format(SGroupName,vpcid))
				elif int(ch)== 4:
					imageid = input("Enter AMI image ID:")
					instype = input("Enter Instance type:")
					subnetid= input("Eneter subnet ID:")
					sgid = input("Enter Security Group ID:")
					keyname = input("Enter key name:")
					os.system("aws ec2 run-instances — image-id {} — instance-type {} — subnet-id {} — security-group-ids {} — key-name {}".format(imageid,instype,subnetid,sgid,keyname))
				elif int(ch) == 5:
					print("volume created")
		elif int(ch)==10 :
			while True:
				os.system("clear")
				print('''\t -.-.-.-.-.-Welcome-.-.-.-.-.-.-.-.-.
				1. Configure system as namenode
				2. Configure system as datanode
				3. Start Namenode 
				4. Start Datanode 
				5. Fetch the report
				6. Exit
				''')

				os.system("tput setaf 3")
				print("Enter Your Choice:",end="")
				ch=input()
				os.system("tput setaf 2")
				print(ch)
				
		
				if int(ch) == 1:
					# Configuration of hdfs-site.xml file
					os.chdir("/etc/hadoop/")
					myfile1 = open("hdfs-site.xml","w")
					myfile1.write('<?xml version="1.0"?>\n')
					myfile1.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
					myfile1.write("<!-- Put site-specific property overrides in this file. -->\n\n")
					myfile1.write("<configuration>\n")
					myfile1.write("<property>\n")
					myfile1.write("<name>dfs.name.dir</name>\n")
					myfile1.write("<value>/namenode</value>\n")
					myfile1.write("</property>\n")
					myfile1.write("</configuration>\n")
					myfile1.close()

	# Extracting the IP address of the system 
					os.system("ifconfig enp0s3 | grep -E 'inet.[0-9]' | grep -v '127.0.0.1' | awk '{ print $2}' > ips.txt")

					myfile = open("ips.txt")
					content = myfile.read()
					ips = content.split("\n")
					myfile.close()
					ip = ips[0]

	# Configuration of the core-site.xml file
					os.chdir("/etc/hadoop/")
					myfile2 = open("core-site.xml","w")
					myfile2.write('<?xml version="1.0"?>\n')
					myfile2.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
					myfile2.write("<!-- Put site-specific property overrides in this file. -->\n\n")
					myfile2.write("<configuration>\n")
					myfile2.write("<property>\n")
					myfile2.write("<name>fs.default.name</name>\n")
					myfile2.write("<value>hdfs://{ip_address}:9001</value>\n".format(ip_address = ip))
					myfile2.write("</property>\n")
					myfile2.write("</configuration>\n")
					myfile2.close()

	# formating the namenode
					os.system("cd")
					os.system("hadoop namenode -format")

	# Starting the namenode	
					os.system("hadoop-daemon.sh start namenode")
					os.system("jps")
				elif int(ch) == 2:	
					os.chdir("/etc/hadoop/")
					myfile1 = open("hdfs-site.xml","w")
					myfile1.write('<?xml version="1.0"?>\n')
					myfile1.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
					myfile1.write("<!-- Put site-specific property overrides in this file. -->\n\n")
					myfile1.write("<configuration>\n")
					myfile1.write("<property>\n")
					myfile1.write("<name>dfs.data.dir</name>\n")
					myfile1.write("<value>/dn1</value>\n")
					myfile1.write("</property>\n")
					myfile1.write("</configuration>\n")
					myfile1.close()

					ip = input("IP Address of namenode: ")

	# Configuration of the core-site.xml file
					os.chdir("/etc/hadoop/")
					myfile2 = open("core-site.xml","w")
					myfile2.write('<?xml version="1.0"?>\n')
					myfile2.write('<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>\n\n')
					myfile2.write("<!-- Put site-specific property overrides in this file. -->\n\n")
					myfile2.write("<configuration>\n")
					myfile2.write("<property>\n")
					myfile2.write("<name>fs.default.name</name>\n")
					myfile2.write("<value>hdfs://{ip_address}:9001</value>\n".format(ip_address = ip))
					myfile2.write("</property>\n")
					myfile2.write("</configuration>\n")
					myfile2.close()

					# Starting the datanode
					os.system("hadoop-daemon.sh start datanode")
					os.system("jps")
				elif int(ch) == 3:	
					os.system("hadoop-daemon.sh start namenode")
					os.system("jps")
				elif int(ch) == 4:	
					os.system("hadoop-daemon.sh start namenode")
					os.system("jps")
				elif int(ch) == 5:
					os.system("hadoop dfsadmin -report")
				elif int(ch) == 6:
					exit()
				else:
					print("Invalid Choice from menu")
		
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
		elif int(ch)==5:
			while True:
				print(""" 
             1. To Create a New Directory.
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
            14. To Exit
            """)
				os.system("tput setaf 3")
				print("Enter your choice:",end="")
				ch=input()
				os.system("tput setaf 2")
				print(ch)
				if int(ch)== 1:
					dirname = input("Enter Name of directory:")
					os.system("mkdir {}".format(dirname))
				elif int(ch)== 2:
					filename = input("Enter Name of File:")
					os.system("vim {}".format(filename))
				elif int(ch) == 3:
					dirname = input("Enter Name of directory:")
					os.system("rmdir -f {}".format(dirname))
				elif int(ch) == 4:
					os.system("firefox")
				elif int(ch) == 5:
					username = input("Enter Username:")
					os.system("useradd {}".format(username))
				elif int(ch) == 6:
					os.system("ifconfig")
				elif int(ch) == 7:
					os.system("systemctl stop firewalld")
				elif int(ch) == 8:
					os.system("setenforce 0")
				elif int(ch) == 9:
					os.system("""cat > /etc/yum.repos.d/my_stable_repo >>
					[my_stable_repo]
					name = Stable Repo
					baseurl = 'https://myurl/$releasever/stable/Packages/'
					enabled = 1
					gpgcheck = 0
					EOF""")
				elif int(ch) == 10:
					os.system("netstat -tlnp")
				elif int(ch) == 11:
					os.system("ps -aux")
				elif int(ch) == 12:
					processname = input("Enter Process Name")
					os.system("ps -aux | grep -i {}".format(processname))
				elif int(ch) == 13:
					pid = int(input("Enter Process ID/PID:"))
					os.system("kill {}".format(pid))
				elif int(ch) == 14:
					exit()
			input("Enter to continue -> -> ->")
			os.system("clear")
		elif int(ch)==11:
			exit() 
		elif int(ch)==12:
                    while True:
                        print(""" Press1: click 1""")
                        print("Enter you chice:",end="")
                        ch=input()
                        print(ch)
                        if int(ch)==1:
                            os.system("yum repolist")


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
