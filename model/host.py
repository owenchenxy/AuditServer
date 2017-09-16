from utility.MySQLHelper import MySQLHelper
from conf import HOST_INFO_DICT_LIST
class host(MySQLHelper):
    def __init__(self):
        self.table=MySQLHelper()
        
    def add_column(self):
        host_info_list=[]
        host_info=[]
        for dict in HOST_INFO_DICT_LIST:
            host_ip=dict['host_ip']
            hostgroup=dict['hostgroup']
            username=dict['username']
            password=dict['password']
            for i in (host_ip,hostgroup,username,password):
                host_info.append(i)
            host_info_list.append(host_info)
            host_info=[]
        print host_info_list    
        sql="insert into host(host_ip,hostgroup,username,password) values(%s,%s,%s,%s)"
        params=host_info_list
        
        self.table.Modify(sql,params)    
            
    def get_user_pwd(self,host_ip,username):
        sql="select password from host where host_ip=%s and username=%s"
        params=(host_ip,username,)
        password=self.table.GetDataOne(sql, params)['password']
        return password
        
    def get_username_list_by_host_ip(self,host_ip):
        sql="select username from host where host_ip=%s"
        params=(host_ip)
        username_dict_list=self.table.GetDataAll(sql, params)
        username_list=[]
       
        for i in username_dict_list:
            username_list.append(i['username'])
        return username_list    
    
    def get_username_list_all(self):
        sql="select username from host"
        params=()
        username_dict_list=self.table.GetDataAll(sql, params)
        username_list=[]
       
        for i in username_dict_list:
            if i['username'] not in username_list:
                username_list.append(i['username'])
        return username_list 
       
    def get_host_list(self):
        sql="select host_ip from host where username='root'"
        params=[]
        host_dict_list=self.table.GetDataAll(sql, params)
        host_list=[]
        for i in host_dict_list:
            host_list.append(i['host_ip'])
        return host_list
    def get_host_list_by_username(self,username):
        sql="select host_ip from host where username=%s"
        params=[username,]
        host_dict_list=self.table.GetDataAll(sql, params)
        host_list=[]
        for i in host_dict_list:
            host_list.append(i['host_ip'])
        return host_list   
    def get_host_list_by_group(self,hostgroup):
        sql="select host_ip from host where hostgroup=%s and username='root'"
        params=(hostgroup,)
        host_dict_list=self.table.GetDataAll(sql, params)
        host_list=[]
        for i in host_dict_list:
            host_list.append(i['host_ip'])
        return host_list
    
    def get_hostgroup_list_all(self):
        sql="select hostgroup from host"
        params=()
        hostgroup_list=[]
        hostgroup_dict_list=self.table.GetDataAll(sql, params)
        for i in hostgroup_dict_list:
            if i['hostgroup'] not in hostgroup_list:
                hostgroup_list.append(i['hostgroup'])
        return hostgroup_list
    
    def get_hostgroup_list_by_username(self,username):
        sql="select hostgroup from host where username=%s"
        params=(username,)
        hostgroup_list=[]
        hostgroup_dict_list=self.table.GetDataAll(sql, params)
        for i in hostgroup_dict_list:
            if i['hostgroup'] not in hostgroup_list:
                hostgroup_list.append(i['hostgroup'])
        return hostgroup_list
        
