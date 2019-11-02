def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
            #print('swapped')
    #print(i+1)
    return i+1

removeDuplicates([0,0,1,1,1,2,2,3,3,4])

    
