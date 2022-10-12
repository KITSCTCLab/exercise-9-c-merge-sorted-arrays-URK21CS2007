from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  x = nums1[0:m]
  y = nums2[0:n]
  nums1 = x + y
  nums1 = merge_sort(nums1)
  return nums1
  
  
def merge_sort(myList) -> None:
  if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k=0
