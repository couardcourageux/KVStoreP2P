import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "memory"))
from database import MockDatabase


class Router:  
    @classmethod
    def main(self):
        return MockDatabase.size
    
    @classmethod
    def initial(self):
        resps = []
        for i in range(5):
            resps.append(MockDatabase.setEntry(f"test{i}", "oh, un super test"))
        return resps
    
    @classmethod
    def secondStep(self):
        resps = []
        for i in range(5, 12):
            resps.append(MockDatabase.setEntry(f"test{i}", "oh, un super test"))
        return resps
    
    @classmethod
    def getEntries(self):
        resps = []
        for i in range(5):
            resps.append(MockDatabase.getEntry(f"test{i}"))
        return resps
    
    @classmethod
    def deleteEntries(self):
        resps = []
        for i in range(5):
            resps.append(MockDatabase.popEntry(f"test{i}"))
        return resps