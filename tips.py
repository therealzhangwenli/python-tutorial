# 1. Comma ',' with number formulates a tuple
ans = []
ans += 3,
# Same as above
ans += [3]
ans += [3,]
ans += (3,)

# 2. Tailing ',' is allowed in Python
a = [
        1,
        2,
        5, # it's ok to have a tailing ','
    ]

# 3. Add data to list/dict while iteration
queue = [1]
counter = 3
for val in queue: # Queue will print 1,2,2,2
    print(val)
    if counter:
        queue.append(2)
    counter -= 1
# Save thing works for while loop
queue = [1]
counter = 3
i = 0
while i < len(queue):
    print(queue[i])
    if counter:
        queue.append(2)
    counter -= 1
    i += 1

# 4. setdefault
d = {}
d.setdefault(key, value) # Set when key doesn't exist
# Same as above
if key not in d:
    d[key] = value

# 5. lru_cache
from functools import lru_cache
# leetcode 983

# 6. bisect
# leetcode 981

# 7. map, filter, reduce
# map(function_to_apply, list_of_inputs)
items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
# Can be shorten with 'map'
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
number_list = range(-5, 5)
# Convert int to list
num = 1234
arr = list(map(int, str(num)))
# filter
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
# Output: [-5, -4, -3, -2, -1]
# reduce
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# product = 24
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# 8. Random
import random
random.randrange(1, n+1) # random [1, n]

# 9. Dictionary
d = {}
d.get(100, 0) # get value for key=100, if key doesn't exist, return 0

# 10. collections.counter
from collections import Counter
counter = collections.Counter()

# 11. collections.defaultdict
from collections import defaultdict
d1 = defaultdict(int)        # Default value is 0
d2 = defaultdict(list)       # Default value is []
d3 = defaultdict(lambda: 10) # Set default value to 10
# 12. Counter & heapq, nlargest
# leetcode 347
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
# leetcode 692
# when heapify a tuple, (a,b), it's sorted from small to large,
#   first a, then based on current order, sort b
# heappop always pop most priotized element, meaning smallest after sorting above
# 13. Sprague-Grundy 991
# 14. any()
# 15. <> conditional statement
A < B > C # A < B and B > C
# 16. deque
collections.deque
# 17. Lock list length
for i in arr: # forever loop
    arr.append(i)
for i in range(len(arr)): # loop len(arr) times
    arr.append(arr[i])
# 18
# sort a dictionary items | leetcode 692
sorted(d.items(), key=lambda key_val_pair: (-key_val_pair[1], key_val_pair[0]))
# 19. Counter intersection
c1 = Counter([1,2,2,3])
c2 = Counter([1,1,2,3])
c1 & c2 # {1:1, 2:1, 3:1} Intersection with &
# 20. ord() -> chr()
chr(97)  # 'a'
ord('a') # 97
# 21. Compare by length
a, b = sorted((nums1, nums2), key=len) # shorter one will be 'a', longer one will be 'b'
# 22. OrderedDict (LRU)
from collections import OrderedDict
od = OrderDict()
od.popitem(last=True) # last=True -> LIFO, last=False -> FIFO
# 23. all
all()
# 24. iter()
# Use iter() and `in` as iterative search. 1023-camelcase-matching

