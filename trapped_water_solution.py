#	Rain Water Trapped
#	Problem Description

#	Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, 
#	compute how much water it is able to trap after raining.


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def trap(self, A):
	    water_depth=[]
	    left_max=[]
        right_max=[]
	    max_left=A[0]
	    max_right=A[-1]
        for i in A:
            if i>max_left:
                max_left=i
	        left_max.append(max_left)
	        
        for j in range(len(A)-1,-1,-1):
	        if A[j]>max_right:
	            max_right=A[j]
	        right_max.append(max_right)
	   
	    right_max.reverse()
	    
        for i in range(1,len(A)-1):
            x=min(left_max[i-1],right_max[i+1])-A[i]
            if x>0:
                water_depth.append(x)
        return sum(water_depth)
        
        
            
