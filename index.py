from utility.MultiSSH import remote_ssh
def main():
    while True:
        print '''Would you like to login to single host or host group?
                1. Single Host Management
                2. Host Group Management
                '''
        a=raw_input('Choose:')
        if a=='1':
            remote_ssh.single_host_login()
        elif a=='2':
            remote_ssh.muti_ssh()
        else:
            print 'invalid input'
            continue
    
main()