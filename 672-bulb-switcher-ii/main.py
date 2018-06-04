import math
class Solution:
    def bulbSwitch2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        li=[1 for x in range(n)]
        count=1
        for i in range(2,n+1):
            for j in range(i,n+1,i):
                if j%i==0:
                    li[j-1]+=1
            if li[i-1]%2==1:
                count+=1
        return count
    def bulbSwitch(self, n):
        count=1
        if n==0:
            return 0
        for i in range(2,n+1):
            j_c=1
            for j in range(2,int(math.sqrt(i+1))):
                if i%j==0:
                    j_c+=1
            if j_c%2==1:
                count+=1
        return count;
if __name__ == '__main__':
    s=Solution()
    print(s.bulbSwitch(0))
    print(s.bulbSwitch(1))
    print(s.bulbSwitch(2))
    print(s.bulbSwitch(3))
    print(s.bulbSwitch(4))
    print(s.bulbSwitch(5))
    print(s.bulbSwitch(999))
    print(s.bulbSwitch(9999))
    print(s.bulbSwitch(999999))
