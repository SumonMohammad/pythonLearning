def sortColors(nums):

    low , mid , high = 0,0, len(nums)-1

    while mid <= high :
        if nums[mid]==0:
            nums[low], nums[mid]= nums[mid], nums[low]
            low += 1
            mid += 1

            print(nums)
        elif nums[mid]==1:
            mid += 1
            print(nums)
        else:
            nums[mid], nums[high]= nums[high], nums[mid]
            high -= 1
            print(nums)
    return nums

        
        
if __name__ == "__main__":

    nums =[2,1,0,0,1,2]

    print(sortColors(nums))


