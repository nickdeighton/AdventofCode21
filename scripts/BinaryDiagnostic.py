import os.path

with open(os.path.dirname(__file__) + '/../inputs/day3') as f:
    lines = f.readlines()


def find_power():
    epsilon = ""
    gamma = ""

    for i in range(0, 12):
    
        one_count = 0
        zero_count = 0
    
        for line in lines:
        
            curr = int (line[i])
        
            if (curr == 1):
                one_count += 1
            
            else:
                zero_count += 1
            
        if one_count > zero_count:
            epsilon = epsilon + "1"
            gamma = gamma + "0"
    
        else:
            epsilon = epsilon + "0"
            gamma = gamma + "1"

    epsilon_rate = int(epsilon, 2)
    gamma_rate = int(gamma, 2)  
    power_consumption = epsilon_rate * gamma_rate
    
    return power_consumption


def find_lifesupport():
    oxygen = ""
    co2 = ""
    
    one_lines = []
    zero_lines = []
        
    for line in lines:
        
        if (line[0] == '1'):
            one_lines.append(line)
            
        else:
            zero_lines.append(line)   
            
    if len(one_lines) >= len(zero_lines):
                
        oxygen = oxygen + "1"
        oxygen = find_oxygen(one_lines, oxygen, 1)
        
        co2 = co2 + "0"
        co2 = find_co2(zero_lines, co2, 1)
        
    else:
        
        oxygen = oxygen + "0"
        oxygen = find_oxygen(zero_lines, oxygen, 1)
        
        co2 = co2 + "1"
        co2 = find_co2(one_lines, co2, 1)
        
    oxygen_rate = int(oxygen, 2)
    co2_rate = int(co2, 2)  
    life_rate = oxygen_rate * co2_rate
    
    return life_rate

    
def find_oxygen(olines, oxy, i):
    
    one_lines = []
    zero_lines = []
    
    for o in olines:
        
        if (o[i] == '1'):
            one_lines.append(o)
            
        else:
            zero_lines.append(o)
            
    if len(one_lines) >= len(zero_lines):
        oxy = oxy + "1"
        
        if i != 11:
            oxy = find_oxygen(one_lines, oxy, i + 1)
        
    else:
        oxy = oxy + "0"
        
        if i != 11:
            oxy = find_oxygen(zero_lines, oxy, i + 1)  
            
    return oxy

def find_co2(clines, co, i):
    
    one_lines = []
    zero_lines = []
    
    for c in clines:
        
        if (c[i] == '1'):
            one_lines.append(c)
            
        else:
            zero_lines.append(c)
            
    if len(one_lines) <= len(zero_lines):
        co = co + "1"
        
        if i != 11:
            co = find_co2(one_lines, co, i + 1)
        
    else:
        co = co + "0"
        
        if i != 11:
            co = find_co2(zero_lines, co, i + 1)
            
    return co


print(find_power())
print(find_lifesupport())