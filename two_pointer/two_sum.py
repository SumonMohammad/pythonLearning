

def twoSum(nums, target):
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        

        num_to_index[num]=i
       # print( num_to_index[num])

    return []

if __name__ =="__main__":
    nums=[2,3,7,5]

    k = twoSum(nums , 7)

    print(k)