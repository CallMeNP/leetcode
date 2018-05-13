#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 gaohailong <np.liamg@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenNums=len(nums)
        # 将k>lenNums的情况化简
        k=k%lenNums
        if(k==0):
            return
        cycleNum=self.gcd(lenNums,k)
        for cycle_i in range(cycleNum):
            step_i=cycle_i
            step_j=step_i-k
            step_j%=lenNums
            tmp=nums[cycle_i]
            while step_j!=cycle_i:
                nums[step_i]=nums[step_j]
                step_i-=k
                step_j-=k
                step_i%=lenNums
                step_j%=lenNums
            nums[step_i]=tmp
    def gcd(self,a,b):
        if a%b==0:
            return b
        return self.gcd(b,a%b)

if __name__ == "__main__":
    s=Solution()
    s.rotate([1,2,3,4,5,6,7,8,9,10,11,12],8)
    s.rotate([1,2,3,4,5,6,7],3)
    s.rotate([1],3)
