class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s :
            if i == "{" :
                st.append("}")
            elif i == "[":
                st.append("]")
            elif i == "(":
                st.append(")")
            else:
                if  not st or st.pop() != i :
                    return False
        return not st
