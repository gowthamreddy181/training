HACKERRANK :
1. 2D Array (Matrix) :

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Element at row 1, col 2: {matrix[1][2]}")

2. Sparse Array :

sparse_array = {2: 10, 5: 45, 102: 99}
def get_val(idx):
    return sparse_array.get(idx, 0)
print(f"Value at index 5: {get_val(5)}")
print(f"Value at index 20: {get_val(20)}")

3. counting sort 1 :

arr = [1, 4, 1, 2, 7, 5, 2]
count_arr = [0] * 10

for num in arr:
    count_arr[num] += 1

print("Frequency count array:", count_arr)


CODECHEF :

1. REVESE A NUMBER :

num = 12345
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10

print("Reversed Number:", reversed_num)


2. TURBO SORT:

numbers = [34, 12, 89, 5, 56]
numbers.sort()  # In-place optimized sort

print("Sorted Array:", numbers)


3. Lapindrome Check :

def is_lapindrome(s):
    mid = len(s) // 2
    
    # Split into two halves, ignoring the center character if length is odd
    first_half = sorted(s[:mid])
    second_half = sorted(s[mid:] if len(s) % 2 == 0 else s[mid+1:])
    
    return first_half == second_half

print("gaga:", is_lapindrome("gaga"))
print("rotor:", is_lapindrome("rotor"))
print("hello:", is_lapindrome("hello"))

LEETCODE : 

1. Best Time to Buy and Sell Stock :

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

# Example implementation
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", maxProfit(prices))

2. Longest Common Prefix :

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Sort the array to easily compare the most distinct words
    strs.sort()
    first = strs[0]
    last = strs[-1]
    
    i = 0
    # Compare characters between the first and last string
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]

# Example implementation
strs = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longestCommonPrefix(strs))

3. Search Insert Position (Binary Search) :

def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # If not found, 'low' will point to the correct insertion index
    return low

# Example implementation
nums = [1, 3, 5, 6]
print("Index if target is 5:", searchInsert(nums, 5))
print("Index if target is 2:", searchInsert(nums, 2))

