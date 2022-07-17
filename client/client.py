# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:27:38 2022

@author: zjh
"""

import grpc
import logging
import pet_pb2

from pet_pb2_grpc import PetStoreServiceStub

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    channel = grpc.insecure_channel('localhost:50051')
    stub = PetStoreServiceStub(channel)
    print("Welcome to PetStore v1.0! You have several options:\n1.Get a Pet.\n2.Put a Pet.\n3.Delete a Pet.\n4.Exit the Pet Store.\nPlease return the index of the option.")
    
    #根据用户输入读取选项，分别为GetPet,PutPet,DeletePet,Exit
    choice = input("Option:")  
    while(choice != "4"):
        
        #GetPet的客户端部分
        if(choice == "1"):
            petid = input("Which pet do you want to get?(Input its id):")
            response = stub.GetPet(pet_pb2.GetPetRequest(pet_id = petid))
            gPet = response.pet
            #这里定义所有不合法的Pet的类型都为PET_TYPE_UNSPECIFIED
            if(gPet.pet_type == pet_pb2.PET_TYPE_UNSPECIFIED):
                print("No such Pet!")
            else:
                print(gPet)
        #PutPet的客户端部分
        elif(choice == "2"):
            while(True):
                pettype = input("The type of your pet(1-cat 2-dog 3-snake 4-hamster):")
                if(pettype != "1" and pettype != "2" and pettype != "3" and pettype != "4"):
                    print("PetType:1-cat 2-dog 3-snake 4-hamster(input the index of the type)")
                else:
                    if(pettype == "1"):
                        pt = pet_pb2.PET_TYPE_CAT
                    elif(pettype == "2"):
                        pt = pet_pb2.PET_TYPE_DOG
                    elif(pettype == "3"):
                        pt = pet_pb2.PET_TYPE_SNAKE
                    elif(pettype == "4"):
                        pt = pet_pb2.PET_TYPE_HAMSTER
                    break
            petname = input("The name of your pet:")
            response = stub.PutPet(pet_pb2.PutPetRequest(pet_type = pt,name = petname)) 
            print(response.pet)
        #DeletePet的客户端部分
        elif(choice == "3"):
            petid = input("Which pet do you want to delete?(Input its id):")
            response = stub.DeletePet(pet_pb2.DeletePetRequest(pet_id = petid))
            print("Successfully deleted!")

        else:
            print("You should return the index of the option.And\n1.Get a Pet.\n2.Put a Pet.\n3.Delete a Pet.\n4.Exit the Pet Store.")
         
        choice = input("Option:")
            
    #Exit
    print("Thanks for visiting the Pet Store!")


if __name__ == '__main__':
    logging.basicConfig()
    run()