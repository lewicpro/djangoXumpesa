largest_so_far =  float('-inf') 
smallest_so_far = float('inf')
i = 0
while True:

    value = raw_input(">")
    if value == "done":
        break

    try: 
        value = float(value)
        i = i + 1
    except ValueError: 
 
        continue

    if value > largest_so_far:      
            largest_so_far = value
    if value < smallest_so_far:
            smallest_so_far = value
