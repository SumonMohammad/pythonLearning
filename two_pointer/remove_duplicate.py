

def removeDuplicate(nums):

    if not nums:
        return 0
    
    write_index = 0

    for read_index in range(1, len(nums)):

        if nums[read_index] != nums[write_index]:
            write_index+=1

            nums[write_index]=nums[read_index]
    
    return write_index + 1


if __name__ =="__main__":
    nums=[0,0,1,1,2,3,4,4,5,6,7,7,8]

    k = removeDuplicate(nums)

    print(f" k = {k} nums = {nums[:k]}")