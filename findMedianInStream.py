import heapq
class findMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        # MaxHeap is implemented as min heap DS in pyton 
        #logic is divid all received element into 2 half -
        #All element in first Half <= second Half 
    def add(self,num):
            #alway put element first in first half
            heapq.heappush(self.maxHeap, -num)
            #then move from top element from maxHeap to minheap
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            if len(self.minHeap) > len(self.maxHeap):
                 heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
    def findMedain(self) ->float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0]  + self.minHeap[0])/2
        else:
            return -self.maxHeap[0]


'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)

from typing import List
def findPivot(nums,left,right) ->int:
    pivot , fill = nums[right], left
    for i in range(left,right):
          if nums[i] <= pivot:
               print("Swap val with as elem is smaller than pivot", nums[i],pivot)
               #Swap with pivot index 
               nums[fill], nums[i] = nums[i], nums[fill]
               fill +=1
    #after this all element before fill index would be less than pivot
    nums[right], nums[fill] = nums[fill], nums[right]
    #return pivot index
    return fill

def findKthLargestElement(nums:List[int],k:int)->int:
    k = len(nums) -k 
    left , right = 0, len(nums) -1
    print("nums->",nums)
    while left < right:
        pivot = findPivot(nums,left,right)
        print("left:", left, "right:", right,"pivotIdx:",pivot, "k", k )
        if pivot < k:
            right = pivot -1
        elif pivot > k:
             left = pivot + 1
        else:
             break
    return nums[k]
             
        

nums = [3,2,3,1,2,4,5,5,6] 
k = 4 
print("Kth:", k, "largest element:->", findKthLargestElement(nums,k)) 