def flip(c): 
    return '1' if (c == '0') else '0'

def printTwosComplement(bin): 
  
    n = len(bin)  
    ones = ""
    for i in range(n): 
        ones += flip(bin[i])  
   
    ones = list(ones.strip(""))
    twos = list(ones) 
    for i in range(n - 1, -1, -1): 
      
        if (ones[i] == '1'): 
            twos[i] = '0'
        else:          
            twos[i] = '1'
            break
    if (i == -1): 
        twos.insert(0, '1')  
  
    print("2's complement: ", *twos, sep = "") 

if __name__ == '__main__': 
    bin = "1100"
    printTwosComplement(bin.strip("")) 
