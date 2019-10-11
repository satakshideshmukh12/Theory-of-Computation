
  
def flip(c): 
    return '1' if (c == '0') else '0'
def printOneComplement(bin): 
  
    n = len(bin)  
    ones = "" 
  
    for i in range(n): 
        ones += flip(bin[i])  
    ones = list(ones.strip("")) 
    print("1's complement: ", *ones, sep = "") 
if __name__ == '__main__':
 bin=input()
    printOneComplement(bin.strip(""))
