

forwardCount = 0;
depthCount = 0;
currentAim = 0;

with open("inputs/day2") as f:
    
    lines = f.readlines()
    
for line in lines:  
    if "forward" in line:
        num = line.split("forward ")
        forwardCount += int(num[1])
        
        if currentAim != 0:
            depthCount += currentAim * int(num[1])
         
    elif "down" in line:
        num = line.split("down ")
        currentAim += int(num[1])
    
    elif "up" in line:
        num = line.split("up ")
        currentAim -= int(num[1])
        
# print(forwardCount)
# print(depthCount)
print(forwardCount * depthCount)