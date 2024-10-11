def minSwapsCouples(row):
    # make the row of couple in half
    n = len(row) // 2
    
    index_map = {person: i for i, person in enumerate(row)}
    
    swaps = 0
    
    for i in range(0, len(row), 2):
        first_person = row[i]
        second_person = first_person ^ 1  
        
        # If the partner is not already next to the first person
        if row[i + 1] != second_person:
            # Tries finding the partners position
            partner_index = index_map[second_person]
            
            # Swap the person with partner 
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            
            # Updates map after the swap has occurred
            index_map[row[partner_index]] = partner_index
            index_map[row[i + 1]] = i + 1
            
            # Increment the swap count
            swaps += 1
            
    return swaps

# Test case first output should be 1 and next should be 0
print ("Output: ", minSwapsCouples([0, 2, 1, 3]))  
print ("Output: ", minSwapsCouples([3, 2, 0, 1])) 

