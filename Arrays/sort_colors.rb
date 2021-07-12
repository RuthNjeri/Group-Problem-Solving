def sort_colors(nums)
   return nums if nums.length == 1
   quick_sort(nums, 0, nums.length - 1) 
end


def quick_sort(nums, start, stop)
    if start < stop
        pivot_index = pivot(nums, start, stop)
        # left
        quick_sort(nums, start, pivot_index - 1)
        # right
        quick_sort(nums, pivot_index + 1, stop)
    end
    nums
end

def pivot(nums, start, stop)
    pivot_num = start
    current_pivot = start
    
    while start <= stop
        if nums[pivot_num] > nums[start]
            current_pivot += 1
            nums[current_pivot], nums[start] = nums[start], nums[current_pivot]
        end
        start += 1
    end
    
    nums[current_pivot], nums[pivot_num] = nums[pivot_num], nums[current_pivot]
    
    current_pivot
end
