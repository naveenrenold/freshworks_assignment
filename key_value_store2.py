import sys
import os
import datetime
import json
def find_unique_file_name():
    file_path="file1.txt"
    i=1
    while(1):
        if(os.path.isfile(file_path)):
            i=i+1
            file_path=file_path[0:-5]+str(i)+".txt"
        else:
            break
    return file_path        
    
class key_val_store():
    def __init__(self):
        yes_or_no_character=input("Do you want to mention file path.Press Y or N:")
        # yes_or_no_character='n'
        if(yes_or_no_character=='Y' or yes_or_no_character=='y'):
            self.file_path=input("Enter data store path:")
            if(os.path.exists(self.file_path) and not os.path.isfile(self.file_path)):
                print("Path exists")
                file_name=input("Enter file name:")
                self.file_path=self.file_path+"//"+file_name
                if(os.path.isfile(self.file_path)):   
                    print("File already exists")
                else:
                    print("Creating file:")
                    file_pointer=open(self.file_path,'w')
                    file_pointer.close()
            else:
                print("Path doesnt exist.Using default path")
                self.file_path=find_unique_file_name()
                print(os.getcwd()+"\\"+self.file_path)
                file_pointer=open(self.file_path,'w')
                file_pointer.close()
        else:
            self.file_path=find_unique_file_name()
            print(self.file_path)
            file_pointer=open(self.file_path,'w')
            file_pointer.close()
    def create(self,key,value,ttl="-1"):
        if(len(key)>32):
            raise Exception("Error!,size of key greater than 32 chars")
        if(sys.getsizeof(value)>16000):
            raise Exception("Error!,Value is too large")
        if(os.stat(self.file_path).st_size>1000000000):
            raise Exception("File size is greater than 1GB")
        file_pointer=open(self.file_path,'a')
        if(ttl=="-1"):
            file_pointer.write("{}--{}--{}\n".format(key,value,"-1"))
            file_pointer.close()
        else:
            ttl=datetime.datetime.now()+datetime.timedelta(seconds=ttl)
            file_pointer.write("{}--{}--{}\n".format(key,value,ttl))
            file_pointer.close()
    def read(self,search_key):
        self.update()
        file_pointer=open(self.file_path,'r')
        for line in file_pointer.readlines():
            key,value,ttl=line.split("--")
            if(key==search_key):
                file_pointer.close()
                return value
        file_pointer.close()
        return -1
    def delete(self,search_key):
        self.update()
        flag=0
        file_pointer=open(self.file_path,'r')
        lines=file_pointer.readlines()
        file_pointer.close()
        file_pointer=open(self.file_path,'w')
        for line in lines:
            temp_line=line.strip('\n')
            key,value,ttl=temp_line.split('--')
            if(key==search_key):
                flag=1
            else:
                file_pointer.write(line)
        return flag
    def update(self):
        file_pointer=open(self.file_path,'r')
        lines=file_pointer.readlines()
        file_pointer.close()
        file_pointer=open(self.file_path,'w')
        for line in lines:
            temp_line=line.strip('\n')
            key,value,ttl=temp_line.split('--')
            if(ttl=="-1"):
                file_pointer.write(line)
                continue
            #ttl=ttl1+" "+ttl2
            if(datetime.datetime.now()<datetime.datetime.strptime(ttl,"%Y-%m-%d %H:%M:%S.%f")):
                file_pointer.write(line)
            else:
                continue
        file_pointer.close()
        