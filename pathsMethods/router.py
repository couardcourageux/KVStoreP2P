import sys
import os

LOCAL_DIRECTORY = os.getcwd()
sys.path.append(os.path.join(LOCAL_DIRECTORY, "memory"))
sys.path.append(os.path.join(LOCAL_DIRECTORY, "internalTypes"))

from database import MockDatabase, CustomrResp
from routerArgs import PutEntryDtc, PutEntriesDtc, DelGetEntryDtc

class Router:  
    @classmethod
    def main(self):
        return MockDatabase.size
    
    
    
    # @classmethod
    # def getEntries(self):
    #     resps = []
    #     for i in range(5):
    #         resps.append(MockDatabase.getEntry(f"test{i}"))
    #     return resps
    
    
    @classmethod
    def setEntry(self, pe: PutEntryDtc) -> CustomrResp:
        resp = MockDatabase.setEntry(pe.key, pe.val, pe.user_id, pe.rights)
        return resp
    
    @classmethod
    def setEntries(self, pe: PutEntriesDtc) -> CustomrResp:
        resps = []
        for re in pe.putEntries:
            resps.append(MockDatabase.setEntry(re.key, re.val, re.user_id, re.rights))
        return resps
    
    @classmethod
    def delEntry(self, de: DelGetEntryDtc) -> CustomrResp:
        return MockDatabase.popEntry(de.key, de.user_id)
    
    @classmethod
    def getEntry(self, ge: DelGetEntryDtc) -> CustomrResp:
        return MockDatabase.getEntry(ge.key, ge.user_id)
        