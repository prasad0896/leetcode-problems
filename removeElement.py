def removeElement(nums,val):
    i = 0
    for j in range(0,len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i+=1
            #print('swapped')
        print(nums)
    print(i)
    return i

removeElement([3,2,2,3],3)