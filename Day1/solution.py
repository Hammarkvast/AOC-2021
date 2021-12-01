from typing import List

#Part 1
def increasedDepths(depths: List[int]) -> int:
    increases = 0
    index = 1
    while index < len(depths):
        if depths[index] > depths[index - 1]:
            increases+=1
        index+=1
    return increases

#Part 2
def slidingWindow(depths: List[int]):
    index = 0
    window = [0 for x in range(0, len(depths)) if x < len(depths) - 2]
    while index < len(depths) - 2:
        window[index] = depths[index] + depths[index + 1] + depths[index + 2] 
        index+=1
    amount = increasedDepths(window)
    return amount

input = List[int]
with open('input.txt') as f:
    input = [line.rstrip() for line in f]
for i in range(0, len(input)):
    input[i] = int(input[i])


print(f"Part 1 : {increasedDepths(input)}")
print(f"Part 2: {slidingWindow(input)}")