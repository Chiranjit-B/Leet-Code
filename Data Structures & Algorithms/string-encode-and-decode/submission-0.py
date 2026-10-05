class Solution:

    def encode(self, strs: List[str]) -> str:
        temp_str = ""
        for i in strs :
            temp_str += str(len(i))+"#"+i

        return temp_str


#####                                   4#chan5#Apple
    def decode(self, s: str) -> List[str]:

        i,j = 0,0
        temp = ''
        arr = []
        while i < len(s) :
            j = i
            while s[j] != '#' :
                j+=1
            length = int(s[i:j])
            temp   = s[j+1:j+length+1]
            arr.append(temp)
            i = j +  length + 1 
        return arr
        

