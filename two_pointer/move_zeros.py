
def moveZeros(nums):
    if not nums:
        return 0
    
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:

            nums[left], nums[right]= nums[right] ,nums[left]

            left +=1


    return nums


if __name__ =="__main__":
    nums=[0,0,1,1,2,3]

    k = moveZeros(nums)

    print(k)

