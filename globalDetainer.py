import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "memory"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "pathsMethods"))
###


from database import MockDatabase
from router import Router

class GlobalDetainer():
    __localDb = MockDatabase()
    __router = Router()
    
    @classmethod
    def main(self):
        return self.__router.main(self.__localDb)
    
    @classmethod
    def initial(self):
        return self.__router.initial(self.__localDb)
    
    @classmethod
    def secondStep(self):
        return self.__router.secondStep(self.__localDb)
    
    @classmethod
    def getEntries(self):
        return self.__router.getEntries(self.__localDb)
    
    @classmethod
    def deleteEntries(self):
       return self.__router.deleteEntries(self.__localDb)
    