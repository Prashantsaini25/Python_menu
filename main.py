import os
import getpass
os.system("tput setaf 1")

print("\t\t\thii welcome to my TUI")

os.system("tput setaf 5")
print("\t\t\t---------------------")
#os.system("date")

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
	print(""" PRESS OPTION THAT YOU NEED 
        ########################################
        #Press1: # Basic Linux        @ (Menu) @  
        ########################################
	#Press2: # AWS                @ (Menu) @
	########################################
	#Press3: # Hadoop             @ (Menu) @
	########################################
	#Press4: # Docker             @ (Menu) @     
	########################################
	#Press5: # Ansible            @ (Menu) @
	########################################
	#Press6: # To Check IP of system       #
	########################################
	#Press7: # To Create python CGI file   #
	########################################
        #Press8: # To Create Own Python File   #
        ########################################
        #Press9: # To Create Own Terraform Code#
        ########################################
        #Press10:# To configure Webserver      #
        ########################################
        ########################################
        #Press11:# Exit                        # 
	########################################
	########################################""")

	os.system("tput setaf 3")
	print("Enter your choice:",end="")
	ch=input()

	os.system("tput setaf 2")
	print(ch)

	if location=="local":
		if int(ch)==5 :
			while True:
                                print("""
                        ###############################################
                        #Press1 : To Configure Ansible                #
                        ###############################################
                        #Press2 : Run any Playbook                    #
                        ###############################################
                        """)
                                os.system("tput setaf 3")
                                print("Enter Your Ansible Choice:",end="")
                                ch=input()
                                os.system("tput setaf 2")
                                print(ch)
                                if int (ch)== 1:
                                        os.system('pip3 install ansible')
                                elif int(ch)==2:
                                        file=input("Enter Your Ansible File name:")
                                        os.system('ansible playbook {}'.format(file))
		elif int(ch)==4 :
			while True:
                                print("""
                        ###############################################
                        #Press1 :# To Install Docker                  #
                        ###############################################
                        #Press2 :# To Pull Docker Image               #
                        ###############################################
                        #Press3 :# To See all Docker images           #
                        ###############################################
                        #Press4 :# To See all Runining conatiner      #
                        ###############################################
                        #Press5 :# To see inspection of docker        #
                        ###############################################
                        #Press6 :# To install httpd & python in docker#
                        ###############################################
                        #Press7 :# To Stop Docker conatienr           #
                        ###############################################
                        #Press8 :# To Remove any conatiner            #
                        ###############################################
                        #Press9 :# To remove all Conatiner            #
                        ###############################################
                        ###############################################
                        #Press10:# EXIT                               #
                        ###############################################
                        ###############################################
                        """)
                                os.system("tput setaf 3")
                                print("Enter Your Docker Choice:",end="")
                                ch=input()
                                os.system("tput setaf 2")
                                print(ch)
                                if int(ch)== 1:
                                        os.system('yum install docker-ce --nobest -y')
                                elif int(ch)== 2:
                                        image=input("Enter image name:")
                                        os.system('docker pull {}'.format(image))
                                elif int(ch)== 3:
                                        os.system('docker images')
                                elif int(ch)== 4:
                                        os.system('docker ps -a -q)
                                elif int(ch)==5:
                                        Cname=input("Enter conatiner Name:")
                                        os.system('docker inspect {}'.format(Cname))
                                elif int(ch)==6:
                                        DCname = input("Enter Name of Conatiner:")
                                        os.system('docker start {}'.format(DCname))
                                        os.system('docker exec -it {} yum install httpd python3 -y'.format(hn))
                                elif int(ch)==7:
                                        DCname = input("Enter Container name:")
                                        os.system('docker stop {}'.format(DCname))
                                elif int(ch)==8:
                                        DCname = input("Enter Conatiner Name:")
                                        os.system('docker rm {}'.format(DCname))
                                elif int(ch)==9:
                                        os.system("docker rm -f $(docker ps -a -q)")
                                elif int(ch)==10:
                                        exit()
                                else:
                                        print("invalid input")
                        input("Enter the countinue -> -> ->")
                        os.input("clear")
		elif int(ch)==10 :
			os.system("yum install webserver")
		elif int(ch)==2 :
			while True:
				print("""
                        ################################################
			#Press1 : To Configure AWS-CLI                 #
			################################################
			#Press2 : To Configure AWS 	               #
			################################################
			#Press3 : To Create a Key Pair Own AWS         #
                        ################################################
			#Press4 : To Create a Security Group AWS       #
			################################################
			#Press5 : To Launch AWS Instance               #
                        ################################################
			#Press6 : To Create new Volume                 #
 			################################################
 			#Press7 : To Attaced EBS to Instance           #
 			################################################
			#Press8 : To Create S3 Bucket 		       #
			################################################
			#Press9 : To Upload Data in S3                 #
			################################################
			#Press10: To Create CloudFront                 #
			################################################
			#Press11: To Delete Key pair                   #
			################################################
			#Press12: To Deteched EBS volume               #
			################################################
			#Press13: To Stop AWS Instance                 #
			################################################
			#Press14: To Stop Terminate Instance           #
			################################################
			#Press15: To delete data in S3                 #
			################################################
			#Press16: To delete S3 data                    #
			################################################
			################################################
			#Press17: Exit				       #
			################################################
			################################################
			""")
			
				os.system("tput setaf 3")
				print("Enter Your Choice:",end="")
				ch=input()
				os.system("tput setaf 2")
				print(ch)
				if int(ch)== 1:
					os.system("""curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" """)
					os.system('unzip awscliv2.zip')
					os.system('sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin')
				if int(ch)== 2:
					os.system("aws configure")
				elif int(ch) == 3:
					keyname = input("Enter Key Name:")
					os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
				elif int(ch)== 4:
					SGroupName = input("Enter Security Groupname:")
					vpcid = input("Enter VPC ID:")
					os.system('aws ec2 create-security-group --description "security group" --group-name "{}" --vpc-id {}'.format(SGroupName,vpcid))
				elif int(ch)== 5:
					imageid = input("Enter AMI image ID:")
					instype = input("Enter Instance type:")
					subnetid= input("Enter Subnet ID:")
					sgid = input("Enter Security Group ID:")
					keyname = input("Enter key name:")
					os.system("aws ec2 run-instances — image-id {} — instance-type {} — subnet-id {} — security-group-ids {} — key-name {}".format(imageid,instype,subnetid,sgid,keyname))
				elif int(ch) == 6:
					Vtype = input("Enter Your Volume :")
                                        Vsize = input("Enter Volume Size :")
                                        Azone = input("Enter Availability Zone :")
                                        os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(Vtype , Vsize , Azone))
                                elif int(ch) == 7:
                                        Vid = input("Enter Volume ID :")
                                        Iid = input("Enter Instance ID :")
                                        os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(Vid , Iid))
				elif int(ch) == 8:
					Bname = input("Input your unique bucket name:")
					Rname = input("Enter Your Region Name: ")
					os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(Bname , Rname , Rname))
                                elif int(ch) == 9:    
                                        Fpath = input("Enter Full Path of file :")
                                        SBname = input("Enter S3 Bucket Name : ")
                                        Spermissions = input("Enter permissions S3 : ")
                                        os.system('aws s3 cp  {}  s3://{}/  --acl {}'.format(Fpath , SBname , Spermissions))
				elif int(ch) == 10:
					SBname = input("Enter Your S3 Bucket Name :")
					os.system('aws cloudfront create-distribution  --origin-domain-name {}.s3.amazonaws.com'.format(SBname))
				elif int(ch) == 11:
                                        Kname = input("Enter Your Key Name : ")
                                        os.system('aws ec2 delete-key-pair --key-name {}'.format(kname))
      
                                elif int(ch) == 12:
                                        EBSid = input("Enter EBS ID To Detached : ")
                                        os.system('aws ec2 detach-volume --volume-id {}'.format(EBSid))

                                elif int(ch) == 13 :
                                        Iid = input("Enter Instance ID : ")
                                        os.system('aws ec2 stop-instances --instance-ids {}'.format(Iid))
                                elif int(ch) == 14:
                                        Iid = input("Enter Instance ID : ")
                                        os.system('aws ec2 terminate-instances --instance-ids {}'.format(Iid))
                                elif int(ch) == 15:
                                        Oname = input("Enter Name of object :")
                                        Bname = input("Enter S3 Bucket Name : ")
                                        os.system('aws s3 rm s3://{}/{}'.format(Oname , Bname))
                                elif int(ch) == 16:
                                        Bname = input("Enter S3 Bucket Name : ")
                                        Region = input("Enter Region:")
                                        os.system('aws s3api delete-bucket --bucket {} --region {}'.format(Bname,Region))
                                elif int(ch) == 17:
                                        exit()
                                else:
                                        print("Invarid")
                        input("Enter to continue -> -> ->")
			os.system("clear")	 
		elif int(ch)==3 :
			while True:
				os.system("clear")
				print('''\t -.-.-.-.-.-Welcome-.-.-.-.-.-.-.-.-.
				###############################################
				#Press1. # Configure system as namenode       #
				###############################################
				#Press2. # TO Configure system as datanode    #
				###############################################
				#Press3. # To Start Namenode                  #
				###############################################
				#Press4. # To Start Datanode                  #
				###############################################
				#Press5. # To Configure system as client      #
                                ###############################################
				#Press6. # To Check dfsadmin report           #
				###############################################
				#Press7. # TO Upload Data To Hadoop Cluster   #
				###############################################
				#Press8. # To Read File on Hadoop Cluster     #
				###############################################
				#Press9. # To Delete client File              #
				###############################################	
				#Press10.# To Stop Datanode                   #
				###############################################
				#Press11.# To Stop Namenode                   #
				###############################################
				###############################################
				#Press12. # Exit                              #
				###############################################
				###############################################
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
				elif int(ch) == 6:
					os.system("hadoop dfsadmin -report")
				elif int(ch) == 5:
					ip = input("IP Address of namenode: ")
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
				elif int(ch) == 7:
					sfile = input("Path of source file:-")
					dfile = input("Path of destination:-")
					command='hadoop fs -put {} {}'.format(ask1,ask2)
					os.system(a)
				elif int(ch) == 8:
					ip = input("Enter Ip:")
					fname=("Enter File name:")
					os.system('ssh {} hadoop fs -cat /{}'.format(ip,fname))
				elif int(ch) == 9:
					ip =input("Enter Ip:")
					fname=input("Enter File name:")
					os.system('ssh {} hadoop fs -rm /{}'.format(ip,fname))
				elif int(ch) == 10:
					os.system('hadoop-daemon.sh stop datanode')
				elif int(ch) == 11:
					os.system('hadoop-daemon.sh stop namenode')
				elif int(ch) == 12:
					exit()

				else:
					print("Invalid Choice from menu")
                        input("Enter to continue -> -> ->")
			os.system("clear")		
		elif int(ch)==6:
			os.system("ifconfig")
                
		elif int(ch)==7:
			File = "Enter CGI file name:")
			os.system("vi /var/www/cgi-bin/{}".format(File))
		elif int(ch)==8:
                        print("Give your Python file name with .py ectension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))    
			
		elif int(ch)==9:
                        print("Give your file name with .tf extension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))
		elif int(ch)==1:
			while True:
				print("""
             #############################################
             #Press1 :# To Create a New Directory.       #
             #############################################
             #Press2 :# To Open Text Editor              #
             #############################################
             #Press3 :# To Delete the Directory          #
             #############################################
             #Press4 :# To Open Firefox Browser          #
             #############################################
             #Press5 :# To Create a New User             #
             #############################################
             #Press6 :# To Check IP of System            #
             #############################################
             #Press7 :# To Stop Firewall                 #
             #############################################
             #Press8 :# To Set SE Linux Permissive       #
             #############################################
             #Press9 :# To Configure yum                 #
             #############################################
             #Press10:# To Check Running Ports           #
             #############################################
             #Press11:# To Check Running Processes       #
             #############################################
             #Press12:# To Check PID of Process          #
             #############################################
             #Press13:# To Kill Process                  #
             #############################################
             #Press14:# To Transfer Firefox cookies      #
             #############################################
             #############################################
             #Press15:# To Exit                          #
             #############################################
             #############################################
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
					import subprocess
					remote=input("Enter IP of Targeted System:-")
					remotepass=input("Enter Remote pass:-")
					command = 'sshpass -p {} scp {}:/root/.mozilla/firefox/nr674kcx.default/cookies.sqlite /root/.mozilla/firefox/nr674cx.default.default/cookies.sqlite'.format(remote,remotepass)
				elif int(ch) == 15:
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
		if int(ch)==5 :
			while True:
                                print("""
                        ###############################################
                        #Press1 : To Configure Ansible                #
                        ###############################################
                        #Press2 : Run any Playbook                    #
                        ###############################################
                        """)
                                os.system("tput setaf 3")
                                print("Enter Your Ansible Choice:",end="")
                                ch=input()
                                os.system("tput setaf 2")
                                print(ch)
                                if int (ch)== 1:
                                        os.system('pip3 install ansible')
                                elif int(ch)==2:
                                        file=input("Enter Your Ansible File name:")
                                        os.system('ansible playbook {}'.format(file))
		elif int(ch)==4 :
			while True:
                                print("""
                        ###############################################
                        #Press1 :# To Install Docker                  #
                        ###############################################
                        #Press2 :# To Pull Docker Image               #
                        ###############################################
                        #Press3 :# To See all Docker images           #
                        ###############################################
                        #Press4 :# To See all Runining conatiner      #
                        ###############################################
                        #Press5 :# To see inspection of docker        #
                        ###############################################
                        #Press6 :# To install httpd & python in docker#
                        ###############################################
                        #Press7 :# To Stop Docker conatienr           #
                        ###############################################
                        #Press8 :# To Remove any conatiner            #
                        ###############################################
                        #Press9 :# To remove all Conatiner            #
                        ###############################################
                        ###############################################
                        #Press10:# EXIT                               #
                        ###############################################
                        ###############################################
                        """)
                                os.system("tput setaf 3")
                                print("Enter Your Docker Choice:",end="")
                                ch=input()
                                os.system("tput setaf 2")
                                print(ch)
                                if int(ch)== 1:
                                        os.system('yum install docker-ce --nobest -y')
                                elif int(ch)== 2:
                                        image=input("Enter image name:")
                                        os.system('docker pull {}'.format(image))
                                elif int(ch)== 3:
                                        os.system('docker images')
                                elif int(ch)== 4:
                                        os.system('docker ps -a -q)
                                elif int(ch)==5:
                                        Cname=input("Enter conatiner Name:")
                                        os.system('docker inspect {}'.format(Cname))
                                elif int(ch)==6:
                                        DCname = input("Enter Name of Conatiner:")
                                        os.system('docker start {}'.format(DCname))
                                        os.system('docker exec -it {} yum install httpd python3 -y'.format(hn))
                                elif int(ch)==7:
                                        DCname = input("Enter Container name:")
                                        os.system('docker stop {}'.format(DCname))
                                elif int(ch)==8:
                                        DCname = input("Enter Conatiner Name:")
                                        os.system('docker rm {}'.format(DCname))
                                elif int(ch)==9:
                                        os.system("docker rm -f $(docker ps -a -q)")
                                elif int(ch)==10:
                                        exit()
                                else:
                                        print("invalid input")
                        input("Enter the countinue -> -> ->")
                        os.input("clear")
		elif int(ch)==10 :
			os.system("yum install webserver")
		elif int(ch)==2 :
			while True:
				print("""
                        ################################################
			#Press1 : To Configure AWS-CLI                 #
			################################################
			#Press2 : To Configure AWS 	               #
			################################################
			#Press3 : To Create a Key Pair Own AWS         #
                        ################################################
			#Press4 : To Create a Security Group AWS       #
			################################################
			#Press5 : To Launch AWS Instance               #
                        ################################################
			#Press6 : To Create new Volume                 #
 			################################################
 			#Press7 : To Attaced EBS to Instance           #
 			################################################
			#Press8 : To Create S3 Bucket 		       #
			################################################
			#Press9 : To Upload Data in S3                 #
			################################################
			#Press10: To Create CloudFront                 #
			################################################
			#Press11: To Delete Key pair                   #
			################################################
			#Press12: To Deteched EBS volume               #
			################################################
			#Press13: To Stop AWS Instance                 #
			################################################
			#Press14: To Stop Terminate Instance           #
			################################################
			#Press15: To delete data in S3                 #
			################################################
			#Press16: To delete S3 data                    #
			################################################
			################################################
			#Press17: Exit				       #
			################################################
			################################################
			""")
			
				os.system("tput setaf 3")
				print("Enter Your Choice:",end="")
				ch=input()
				os.system("tput setaf 2")
				print(ch)
				if int(ch)== 1:
					os.system("""curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" """)
					os.system('unzip awscliv2.zip')
					os.system('sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin')
				if int(ch)== 2:
					os.system("aws configure")
				elif int(ch) == 3:
					keyname = input("Enter Key Name:")
					os.system("aws ec2 create-key-pair --key-name {}".format(keyname))
				elif int(ch)== 4:
					SGroupName = input("Enter Security Groupname:")
					vpcid = input("Enter VPC ID:")
					os.system('aws ec2 create-security-group --description "security group" --group-name "{}" --vpc-id {}'.format(SGroupName,vpcid))
				elif int(ch)== 5:
					imageid = input("Enter AMI image ID:")
					instype = input("Enter Instance type:")
					subnetid= input("Enter Subnet ID:")
					sgid = input("Enter Security Group ID:")
					keyname = input("Enter key name:")
					os.system("aws ec2 run-instances — image-id {} — instance-type {} — subnet-id {} — security-group-ids {} — key-name {}".format(imageid,instype,subnetid,sgid,keyname))
				elif int(ch) == 6:
					Vtype = input("Enter Your Volume :")
                                        Vsize = input("Enter Volume Size :")
                                        Azone = input("Enter Availability Zone :")
                                        os.system('aws ec2 create-volume --volume-type {} --size {} --availability-zone {}'.format(Vtype , Vsize , Azone))
                                elif int(ch) == 7:
                                        Vid = input("Enter Volume ID :")
                                        Iid = input("Enter Instance ID :")
                                        os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(Vid , Iid))
				elif int(ch) == 8:
					Bname = input("Input your unique bucket name:")
					Rname = input("Enter Your Region Name: ")
					os.system('aws s3api create-bucket --bucket {} --region {} --create-bucket-configuration LocationConstraint={}'.format(Bname , Rname , Rname))
                                elif int(ch) == 9:    
                                        Fpath = input("Enter Full Path of file :")
                                        SBname = input("Enter S3 Bucket Name : ")
                                        Spermissions = input("Enter permissions S3 : ")
                                        os.system('aws s3 cp  {}  s3://{}/  --acl {}'.format(Fpath , SBname , Spermissions))
				elif int(ch) == 10:
					SBname = input("Enter Your S3 Bucket Name :")
					os.system('aws cloudfront create-distribution  --origin-domain-name {}.s3.amazonaws.com'.format(SBname))
				elif int(ch) == 11:
                                        Kname = input("Enter Your Key Name : ")
                                        os.system('aws ec2 delete-key-pair --key-name {}'.format(kname))
      
                                elif int(ch) == 12:
                                        EBSid = input("Enter EBS ID To Detached : ")
                                        os.system('aws ec2 detach-volume --volume-id {}'.format(EBSid))

                                elif int(ch) == 13 :
                                        Iid = input("Enter Instance ID : ")
                                        os.system('aws ec2 stop-instances --instance-ids {}'.format(Iid))
                                elif int(ch) == 14:
                                        Iid = input("Enter Instance ID : ")
                                        os.system('aws ec2 terminate-instances --instance-ids {}'.format(Iid))
                                elif int(ch) == 15:
                                        Oname = input("Enter Name of object :")
                                        Bname = input("Enter S3 Bucket Name : ")
                                        os.system('aws s3 rm s3://{}/{}'.format(Oname , Bname))
                                elif int(ch) == 16:
                                        Bname = input("Enter S3 Bucket Name : ")
                                        Region = input("Enter Region:")
                                        os.system('aws s3api delete-bucket --bucket {} --region {}'.format(Bname,Region))
                                elif int(ch) == 17:
                                        exit()
                                else:
                                        print("Invarid")
                        input("Enter to continue -> -> ->")
			os.system("clear")	 
		elif int(ch)==3 :
			while True:
				os.system("clear")
				print('''\t -.-.-.-.-.-Welcome-.-.-.-.-.-.-.-.-.
				###############################################
				#Press1. # Configure system as namenode       #
				###############################################
				#Press2. # TO Configure system as datanode    #
				###############################################
				#Press3. # To Start Namenode                  #
				###############################################
				#Press4. # To Start Datanode                  #
				###############################################
				#Press5. # To Configure system as client      #
                                ###############################################
				#Press6. # To Check dfsadmin report           #
				###############################################
				#Press7. # TO Upload Data To Hadoop Cluster   #
				###############################################
				#Press8. # To Read File on Hadoop Cluster     #
				###############################################
				#Press9. # To Delete client File              #
				###############################################	
				#Press10.# To Stop Datanode                   #
				###############################################
				#Press11.# To Stop Namenode                   #
				###############################################
				###############################################
				#Press12. # Exit                              #
				###############################################
				###############################################
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
				elif int(ch) == 6:
					os.system("hadoop dfsadmin -report")
				elif int(ch) == 5:
					ip = input("IP Address of namenode: ")
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
				elif int(ch) == 7:
					sfile = input("Path of source file:-")
					dfile = input("Path of destination:-")
					command='hadoop fs -put {} {}'.format(ask1,ask2)
					os.system(a)
				elif int(ch) == 8:
					ip = input("Enter Ip:")
					fname=("Enter File name:")
					os.system('ssh {} hadoop fs -cat /{}'.format(ip,fname))
				elif int(ch) == 9:
					ip =input("Enter Ip:")
					fname=input("Enter File name:")
					os.system('ssh {} hadoop fs -rm /{}'.format(ip,fname))
				elif int(ch) == 10:
					os.system('hadoop-daemon.sh stop datanode')
				elif int(ch) == 11:
					os.system('hadoop-daemon.sh stop namenode')
				elif int(ch) == 12:
					exit()

				else:
					print("Invalid Choice from menu")
                        input("Enter to continue -> -> ->")
			os.system("clear")		
		elif int(ch)==6:
			os.system("ifconfig")
                
		elif int(ch)==7:
			File = "Enter CGI file name:")
			os.system("vi /var/www/cgi-bin/{}".format(File))
		elif int(ch)==8:
                        print("Give your Python file name with .py ectension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))    
			
		elif int(ch)==9:
                        print("Give your file name with .tf extension:",end="")
                        Filename= input()
                        os.system("vi {}".format(Filename))
		elif int(ch)==1:
			while True:
				print("""
             #############################################
             #Press1 :# To Create a New Directory.       #
             #############################################
             #Press2 :# To Open Text Editor              #
             #############################################
             #Press3 :# To Delete the Directory          #
             #############################################
             #Press4 :# To Open Firefox Browser          #
             #############################################
             #Press5 :# To Create a New User             #
             #############################################
             #Press6 :# To Check IP of System            #
             #############################################
             #Press7 :# To Stop Firewall                 #
             #############################################
             #Press8 :# To Set SE Linux Permissive       #
             #############################################
             #Press9 :# To Configure yum                 #
             #############################################
             #Press10:# To Check Running Ports           #
             #############################################
             #Press11:# To Check Running Processes       #
             #############################################
             #Press12:# To Check PID of Process          #
             #############################################
             #Press13:# To Kill Process                  #
             #############################################
             #Press14:# To Transfer Firefox cookies      #
             #############################################
             #############################################
             #Press15:# To Exit                          #
             #############################################
             #############################################
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
					import subprocess
					remote=input("Enter IP of Targeted System:-")
					remotepass=input("Enter Remote pass:-")
					command = 'sshpass -p {} scp {}:/root/.mozilla/firefox/nr674kcx.default/cookies.sqlite /root/.mozilla/firefox/nr674cx.default.default/cookies.sqlite'.format(remote,remotepass)
				elif int(ch) == 15:
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
