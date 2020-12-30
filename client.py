# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:20:39 2020

@author: acchr
"""

import key_value_store2
import threading

def use_key_value_store():
        key_value_store_object=key_value_store2.key_val_store()
        while(1):
            option=input("Select an option:\n1.Create\n2.Read\n3.Delete\n4.Exit\n->")
            if(option=='1'):
                key=input("Enter the key:")
                if(key_value_store_object.read(key)!=-1):
                    print("Error:Key already exists")
                    continue
                value=str(input("Enter the value:"))
                y_or_no_char=input("Do you want to enter Time to Live:\nPress Y or N:")
                if(y_or_no_char=='Y' or y_or_no_char=='y'):
                    ttl=int(input("Enter the Time to Live(in secs):"))
                    try:
                        key_value_store_object.create(key,value,ttl)
                    except Exception as e:
                        print("Exception msg:",e)
                else:
                    try:
                        key_value_store_object.create(key,value)
                    except Exception as e:
                        print("Exception msg:",e)
            elif(option=='2'):
                key=input("Enter the key to search:")
                value=key_value_store_object.read(key)
                if(value==-1):
                    print("Key not found in file storage")
                else:
                    print("Value is ",value)
            elif(option=='3'):
                key=input("Enter the key to delete:")
                flag=key_value_store_object.delete(key)
                if(flag==0):
                    print("Key not found in file storage")
                else:
                    print("Key value pair deleted")
            elif(option=='4'):
                break
            else:
                print("Enter a valid option from 1 to 4")
        print("Thank you for using the software:)")
class thread_implementation_class(threading.Thread):
    def __init__(self,ThreadId,name):
        threading.Thread.__init__(self)
        self.ThreadId=ThreadId
        self.name=name
    def run(self):
        print("Starting Thread:",self.name)
        use_key_value_store()
        print("Finishing Thread:",self.name)
        

use_key_value_store()


