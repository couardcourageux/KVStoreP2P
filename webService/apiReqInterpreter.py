from dataclasses import dataclass
import sys
import os

LOCAL_DIRECTORY = os.getcwd()
WEB_SERVICE = os.path.join(LOCAL_DIRECTORY, "webService")


sys.path.append(os.path.join(WEB_SERVICE, "apiTypes"))
sys.path.append(os.path.join(WEB_SERVICE, "pathMethods"))
###

from putRequests import SetEntry, SetEntries, SetEntryBase, DelGetEntry
from routerArgs import PutEntryDtc, PutEntriesDtc, DelGetEntryDtc

class ApiReqInterpret:
    ### SetEntry Family############

    @classmethod
    def processPutEntryBase(self, entry: SetEntryBase) -> tuple:
        key, val = entry.key, entry.value
        rights = (entry.public_r, entry.public_w)
        return (key, val, rights)
    
    @classmethod
    def processPutEntry(self, req: SetEntry) -> PutEntryDtc:
        user_id = req.user_id
        key, val, rights = ApiReqInterpret.processPutEntryBase(req.entry)
        return PutEntryDtc(key, val, user_id, rights)
    
    @classmethod
    def processPutEntries(self, req: SetEntries) -> PutEntriesDtc:
        entries = []
        for r in req.entries:
            key, val, rights = ApiReqInterpret.processPutEntryBase(r)
            entries.append(PutEntryDtc(key, val, req.user_id, rights))
        return PutEntriesDtc(entries)
    
    #############################
    ### delEntry Family############
    @classmethod
    def processDelGetEntry(self, req: DelGetEntry) -> DelGetEntryDtc:
        return DelGetEntryDtc(req.key, req.user_id)

