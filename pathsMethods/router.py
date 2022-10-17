


class Router:  
    @classmethod
    def main(self, db):
        return db.size
    
    @classmethod
    def initial(self, db):
        resps = []
        for i in range(5):
            resps.append(db.setEntry(f"test{i}", "oh, un super test"))
        return resps
    
    @classmethod
    def secondStep(self, db):
        resps = []
        for i in range(5, 12):
            resps.append(db.setEntry(f"test{i}", "oh, un super test"))
        return resps
    
    @classmethod
    def getEntries(self, db):
        resps = []
        for i in range(5):
            resps.append(db.getEntry(f"test{i}"))
        return resps
    
    @classmethod
    def deleteEntries(self, db):
        resps = []
        for i in range(5):
            resps.append(db.popEntry(f"test{i}"))
        return resps