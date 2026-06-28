import time
import bisect

start_time = time.perf_counter()

s = 'dsahjpjauf'
s2 = ('ahjpjau', 'ja', 'ahbwzqqnuk', 'tnnlanowax')

s1numerical_map = {}
for i, char in enumerate(s):
    s1numerical_map.setdefault(char, []).append(i)

result = []

for word in s2:
    current_index = -1
    is_valid = True
    
    for char in word:       
        if char not in s1numerical_map:
            is_valid = False
            break
            
        char_indices = s1numerical_map[char]
        
        pos = bisect.bisect_right(char_indices, current_index)
        
        if pos < len(char_indices):
            current_index = char_indices[pos]
        else:
            
            is_valid = False
            break
            
    if is_valid:
        result.append(word)

print("Valid subsequences:", result)
print(f"Total found: {len(result)}")
print(f"Time taken: {time.perf_counter() - start_time:.6f} seconds")