"""
    Leetcode #166
"""


class Solution:
    # Solution copied
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n=numerator
        d=denominator

        sign=1
        if n<0 and d>0:
            sign=-1
        if n>0 and d<0:
            sign=-1

        n=abs(n)
        d=abs(d)

        if n%d==0:
            if sign==-1:
                return '-'+str(n//d)
            return str(n//d)

        s=""

        if n>d:
            s+=str(n//d)
            n-=(n//d)*d
        else:
            s+='0'

        s+='.'

        di={}
        pos=0
        q=-1

        while n%d!=0:
            di.update({n:pos})
            pos+=1
            n=n*10
            s+=str(n//d)
            n-=(n//d)*d
            if n in di:
                q=di[n]
                break

        add=s.find('.')+1
        if q!=-1:
            s=s[:q+add]+'('+ s[q+add:]+')'
        if sign==-1:
            s='-'+s
        return s



if __name__ == "__main__":

    solution = Solution()

    assert solution.fractionToDecimal(1, 2) == "0.5"
    assert solution.fractionToDecimal(2, 1) == "2"
    assert solution.fractionToDecimal(2, 3) == "0.(6)"
