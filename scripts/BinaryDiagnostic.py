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
    
    for i in range(0, 12):
    
        one_count = 0
        zero_count = 0
    
        for line in lines:
        
            curr = int (line[i])
        
            if (curr == 1):
                one_count += 1
                one_lines.add(line)
                
            
            else:
                zero_count += 1
                zero_lines.add(line)
            
        if one_count > zero_count:
            epsilon = epsilon + "1"
            gamma = gamma + "0"
    
        else:
            epsilon = epsilon + "0"
            gamma = gamma + "1"
    
    
print(find_power())

print(find_lifesupport())