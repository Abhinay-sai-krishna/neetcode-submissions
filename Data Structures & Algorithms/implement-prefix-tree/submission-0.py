class PrefixTree:

    def __init__(self):
        self.node={}

    def insert(self, word: str) -> None:
        r=self.node
        for i in word:
            if i not in r:
                r[i]={}
            r=r[i]
        r['*']=''        
    def search(self, word: str) -> bool:
        r=self.node
        for i in word:
            if i not in r:
                return False
            r=r[i]
        if '*' in r:
            return True
        return False    
    def startsWith(self, prefix: str) -> bool:
        r=self.node
        for i in prefix:
            if i not in r:
                return False
            r=r[i]
        return True        
        
        