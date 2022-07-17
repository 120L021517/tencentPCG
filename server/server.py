# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:48:03 2022

@author: zjh
"""

import grpc
import logging
from concurrent import futures
import pet_pb2
from pet_pb2_grpc import PetStoreServiceServicer,add_PetStoreServiceServicer_to_server
import data


class PetsServicer(PetStoreServiceServicer):
    #首先生成一个存储pets的list
    pPets = data.pets()
    #GetPet的服务器端实现
    def GetPet(self, request, context):
        gPet = self.pPets.get_pet(request.pet_id)
        #将数字字符转换为PetType
        if(gPet.PetType == "1"):
            pt = pet_pb2.PET_TYPE_CAT
        elif(gPet.PetType == "2"):
            pt = pet_pb2.PET_TYPE_DOG
        elif(gPet.PetType == "3"):
            pt = pet_pb2.PET_TYPE_SNAKE
        elif(gPet.PetType == "4"):
            pt = pet_pb2.PET_TYPE_HAMSTER
        else:
            pt = pet_pb2.PET_TYPE_UNSPECIFIED
        p = pet_pb2.Pet(pet_type = pt,pet_id = gPet.PetID,name = gPet.PetName)
        return pet_pb2.GetPetResponse(pet = p)
    #PutPet的服务器端实现     
    def PutPet(self, request, context):
        pettype = request.pet_type
        petname = request.name
        #将PetType转换为数字字符
        if(pettype == pet_pb2.PET_TYPE_CAT):
            pt = "1"
        elif(pettype == pet_pb2.PET_TYPE_DOG):
            pt = "2"
        elif(pettype == pet_pb2.PET_TYPE_SNAKE):
            pt = "3"
        elif(pettype == pet_pb2.PET_TYPE_HAMSTER):
            pt = "4"
        pPet = self.pPets.put_pet(pt, petname)
        #将数字字符装欢为PetType
        if(pPet.PetType == "1"):
            pt = pet_pb2.PET_TYPE_CAT
        elif(pPet.PetType == "2"):
            pt = pet_pb2.PET_TYPE_DOG
        elif(pPet.PetType == "3"):
            pt = pet_pb2.PET_TYPE_SNAKE
        elif(pPet.PetType == "4"):
            pt = pet_pb2.PET_TYPE_HAMSTER
        p = pet_pb2.Pet(pet_type = pt,pet_id = pPet.PetID,name = pPet.PetName)
        return pet_pb2.PutPetResponse(pet = p)
    #DeletePet的服务器端实现 
    def DeletePet(self, request, context):
        self.pPets.del_pet(request.pet_id)
        return pet_pb2.DeletePetResponse()
   
        
   
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PetStoreServiceServicer_to_server(PetsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()


