# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 17:58:57 2022

@author: zjh
"""


class pet:
    PetType = "0"
    PetID = "0"
    PetName = "default"
    
class pets:
    petslist = []
    
    #在初始化函数里读入文件里的pets信息
    def __init__(self):
        file = open("data.txt",'r')
        rawlines = file.readlines()
        lines = []
        for line in rawlines:
            lines.append(line.strip('\n'))
        i = 1
        for item in lines:
            if(i == 1):  
                self.petslist.append(pet())
                self.petslist[len(self.petslist)-1].PetType = item
                i = 2
            elif(i == 2):
                self.petslist[len(self.petslist)-1].PetID = item
                i = 3
            else:
                self.petslist[len(self.petslist)-1].PetName = item            
                i = 1      
        file.close()
    
    #GetPet的底层实现
    def get_pet(self,petid):
        answer = 0
        for i in range(len(self.petslist)):
            if(self.petslist[i].PetID == petid):
                answer = i
        return self.petslist[answer]
    
    #PutPet的底层实现
    def put_pet(self,pettype,petname):
        newpet = pet()
        newpet.PetType = pettype
        newpet.PetName = petname
        
        #给新的Pet分配ID，如果之前因为Delete操作存在空位，则新的Pet填补空位，否则加入到列表的末尾
        flag = 0     
        for i in range(len(self.petslist)):
            if(self.petslist[i].PetID != str(i)):
                newpet.PetID = str(i)
                flag = 1
                break
        if(flag == 0):
            newpet.PetID = str(len(self.petslist))
        self.petslist.insert(int(newpet.PetID),newpet)
        #用新的Pets列表覆盖原文件
        file = open("data.txt",'w')
        for i in range(len(self.petslist)):
            file.write(self.petslist[i].PetType + "\n")
            file.write(self.petslist[i].PetID + "\n")
            file.write(self.petslist[i].PetName + "\n")
        file.close()
        return newpet
    #DeletePet的底层实现，删除成功返回1，否则返回-1
    def del_pet(self,petid):
        answer = -1
        for i in range(len(self.petslist)):
            if(self.petslist[i].PetID == petid):
                self.petslist.pop(i)
                answer = 1
                break
        #将删除之后的Pets列表覆盖原文件
        file = open("data.txt",'w')
        for i in range(len(self.petslist)):
            file.write(self.petslist[i].PetType + "\n")
            file.write(self.petslist[i].PetID + "\n")
            file.write(self.petslist[i].PetName + "\n")
        file.close()
        return answer
