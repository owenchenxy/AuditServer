from threading import Thread
from paramiko_audit.demos.demo import demo_func
from utility.choose_username_hostname import username_to_login, host_to_login,host_list_to_login
from model.host import host
import paramiko
import time
import threading


class remote_ssh(object):

    event=threading.Event()
    event2=threading.Event()
    lock=threading.Lock()    
    @staticmethod   
    def single_host_login():
        username=username_to_login()
        hostname=host_to_login(username)
        print username
        print hostname
        demo_func(username,hostname)
    @staticmethod
    def muti_ssh():
        global cmd
        global username
        global hostgroup
        username=username_to_login()
        host_list_group=host_list_to_login(username)
        hostgroup=host_list_group[1]
        host_list=host_list_group[0]
        cmd='cd'
        global host_amount
        host_amount=len(host_list)
        t_master=Thread(target=remote_ssh.give_cmd,args=())
        t_master.start()
        for hostname in host_list:
            t_slave=Thread(target=remote_ssh.para_ssh,args=(hostname,username))
            t_slave.start()
        remote_ssh.event2.set()
        t_master.join()
           
        
    @staticmethod
    def give_cmd():
        global cmd
        global username
        global hostgroup
        global host_amount
        global thread_counter
        while True:
            remote_ssh.event2.wait()
            remote_ssh.event2.clear()
            thread_counter=host_amount
            cmd=raw_input('%s@%s hostgroup:#'%(username,hostgroup))
            #print remote_ssh.event.isSet()
            remote_ssh.event.set()
            if cmd=='exit':
                break
            
    @staticmethod
    def para_ssh(hostname,username):
        global cmd
        global thread_counter
        password=host().get_user_pwd(hostname,username)    
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,22,username, password)

        with open ("/auditLog","a+b") as f:
            while True:
                remote_ssh.event.wait()
                remote_ssh.event.clear()
                timestamp=time.strftime("%Y-%m-%d %X")
                record='%s@%s %s %s'%(username,hostname,timestamp,cmd+'\n')
                f.write(record)
                stdin, stdout, stderr = ssh.exec_command(cmd)
                try:
                    for line in stderr.readlines():
                        print line,
                except Exception:
                    print "command successfully executed"
                finally:
                    remote_ssh.lock.acquire()
                    thread_counter-=1
                    remote_ssh.lock.release()
                    if thread_counter==0:
                        remote_ssh.event2.set()
                if cmd=='exit':
                    break
                
        ssh.close()           
#para_ssh('192.168.0.104','root')