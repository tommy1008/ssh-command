import paramiko
def connect(hostname,port,username,key,commands:[]):
	for command in commands:
		print(command)
	k = paramiko.RSAKey.from_private_key_file(key)
	c = paramiko.SSHClient()
	c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print("connecting") 
	c.connect( hostname = hostname, port=port,username = username, pkey = k )
	print ("connected")
	commands.append(commands)
	for command in commands:
		print ("Executing {}".format( command ))
		stdin , stdout, stderr = c.exec_command(command)
		print (stdout.read())
		print( "Errors")
		print (stderr.read())
	c.close()