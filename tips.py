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
