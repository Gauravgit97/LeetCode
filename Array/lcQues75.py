'''
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively. You must solve this problem without using the library's sort function.
'''

### Approch 1:
return nums.sort()


### Approch 2:
        red,white,blue = 0,0,0
        for i in nums:
            if i==0:
                red +=1
            elif i==1:
                white +=1
            elif i==2:
                blue +=1
        i = 0
        n = len(nums)
        del nums[:] #only because nums is static and nums will print 
        while i<n:
            if red>0:
                nums.append(0)
                red -=1
            elif white>0:
                nums.append(1)
                white -=1
            elif blue>0:
                nums.append(2)
                blue -=1
            i +=1


### Approch 3:
        low = mid = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1