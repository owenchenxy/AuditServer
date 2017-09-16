from model.host import host

def username_to_login():
    host1=host()
    #get the username to login:
    username_list=host1.get_username_list_all()
    seq_u=0
    username_dict=dict()
    for u in username_list:
        seq_u+=1
        print seq_u,'\t',u
        username_dict[seq_u]=u
    while True:
        c=raw_input('choose user to login:')
        try:
            username=username_dict[int(c)]
            break
        except Exception:
            print 'invalid choice'
            continue
    return username

def host_to_login(username):
    host1=host()  
    host_list=host1.get_host_list_by_username(username)
    seq_h=0
    host_dict=dict()
    for h in host_list:
        seq_h+=1
        print seq_h,'\t',h
        host_dict[seq_h]=h
    while True:
        c=raw_input('choose host to login:')
        try:
            host_to_login=host_dict[int(c)]
            break
        except Exception:
            print "invalid choice"
            continue
    return host_to_login

def host_list_to_login(username):
    host1=host()  
    hostgroup_list=host1.get_hostgroup_list_by_username(username)
    seq_hg=0
    hostgroup_dict=dict()
    for hg in hostgroup_list:
        seq_hg+=1
        print seq_hg,'\t',hg
        hostgroup_dict[seq_hg]=hg
    while True:
        c=raw_input('choose hostgroup to login:')
        try:
            hostgroup=hostgroup_dict[int(c)]
            break
        except Exception:
            print "invalid choice"
            continue
    host_list=host1.get_host_list_by_group(hostgroup) 
     
    return host_list,hostgroup

