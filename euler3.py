

def max_prime_factor(val):
    
    while max_factor * max_factor < val: # check numbers up to the square of the val 
        while val % max_factor == 0: # while the number we are checking is a factor
            val = val / max_factor # divide the number until the highest factor is found
        max_factor = max_factor + 1 # try again with a bigger number
        
    return max_factor
    
