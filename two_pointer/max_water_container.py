

def maxContainerArea(nums)-> int:
    left = 0 
    right = len(nums)-1
    maxArea = 0
    while left < right :
        
        d = right - left 
        h = min(nums[left], nums[right])

        area = d*h
        if area> maxArea:
            maxArea=area

        if nums[left]<nums[right]:
            left +=1
        else:
            right -=1
    

    return maxArea
   

def min(l,r):
    if l<r:
        return l
    else:
        return r



if __name__ =="__main__":
    nums=[2,4,5,9,3]

    k = maxContainerArea(nums)

    print(k)