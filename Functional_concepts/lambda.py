nums=[1,2,3,4,5,6,7,8,9,10]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even) 
odd = list(filter(lambda x: x % 2 != 0, nums))
print(odd) 