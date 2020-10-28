import getopt
import sys
import ssh
import traceback
def main(argv):
	try:
	    instruction = 'main.py  -h <hostname> -p <port> -u <username> -k <key> -c <command>'
	
	    hostname = None
	    port=None
	    username=None
	    key = None
	    command=[]
	    try:
	        opts, args = getopt.getopt(argv, "h:p:u:k:c:")
	
	    except getopt.GetoptError:
	        print(instruction)
	        sys.exit(2)
	    for opt, arg in opts:
	        if opt == '-q':
	            print(instruction)
	            sys.exit()
	        elif opt == '-h':
	            hostname = arg
	        elif opt == '-p':
	            port = arg
	        elif opt == '-u':
	            username = arg
	        elif opt == '-k':
	            key = arg
	        elif opt == '-c':
	            command.append(str(arg))
	    print('hostname: ', hostname)
	    print('port: ', port)
	    print('username: ', username)
	    print('key: ', key)
	    print('command: ', command)
	    if hostname is None or username is None:
	        sys.exit()
	    ssh.connect(hostname,port,username,key,command)
	except BaseException:
		print(sys.exc_info()[0])
		print(traceback.format_exc())
		print("Press Enter to continue ...")
		input() 
if __name__ == '__main__':
    main(sys.argv[1:])