import os.path

with open(os.path.dirname(__file__) + '/../inputs/day1') as f:
    lines = f.readlines()

count = 0;
prevSum = int(0);
currSum = int(0);

for line in range(len(lines) - 2):
    
    # currSum = int(line)
    # if line > previous:
    #     count += 1
        
    # previous = line
    
    window_vals = lines[line: line + 3]
    
    for x in window_vals:
        currSum += int(x)
        
    if prevSum > 0 and currSum > prevSum:
        count += 1;
    
    prevSum = currSum
    currSum = 0
    
print(count)

