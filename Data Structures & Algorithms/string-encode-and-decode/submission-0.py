class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(str(len(i)))
            res.append('#')
            res.append(i)
        return "".join(res)    
    def decode(self, s: str) -> List[str]:
        res=[]
        j=0
        while j<len(s):
            temp=j
            while s[temp]!='#':
                temp+=1
            l=int(s[j:temp])
            j=temp+1
            temp=j+l
            res.append(s[j:temp])
            j=temp
        return res       