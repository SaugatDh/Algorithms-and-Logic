import random
my_list = list(range(10))
random.shuffle(my_list)
print("Initial list",my_list)
def linear_search(arr,targetVal):
    count = 0
    for i in range(len(arr)):
        count+=1
        if arr[i] == targetVal:
            return i,count
    return -1,count

result,count = linear_search(my_list,4)

if result != -1:
  print(f"Found at index {result} in turn {count}")
else:
  print("Not found")
