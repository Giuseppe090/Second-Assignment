def longest_common_substring(strs):
    if not strs:
        return ""
    
    
    first_str = strs[0]
    longest_substr = ""
    
    
    for length in range(1, len(first_str) + 1):
        for start in range(len(first_str) - length + 1):
            substring = first_str[start:start + length]
            
            if all(substring in other for other in strs[1:]):
                if len(substring) > len(longest_substr):
                    longest_substr = substring
    
    return longest_substr