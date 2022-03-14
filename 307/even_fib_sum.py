
def even_fib_sum(limit: int):
    prev, curr = 1, 1
    even_sum = 0
    
    while curr <= limit:
        if curr % 2 == 0:
            even_sum += curr
        prev, curr = curr, curr + prev

    return even_sum
        
        
print(even_fib_sum(4000000))