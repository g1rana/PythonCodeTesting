def is_valid_group(group):
    return all('a' <= ch <= 'e' or ch =='?' for ch in group)

def generate_emails(pattern, email, idx, results):
    if idx == len(pattern):
        results.append(email)
        return
    
    if pattern[idx] == '?':
        for ch in 'abcde':
            generate_emails(pattern, email + ch, idx + 1, results)
    else:
        generate_emails(pattern, email + pattern[idx], idx + 1, results)

def solution(pattern):
    groups = pattern.split('@')
    if len(groups) != 2:
        return 0

    local_part, domain_part = groups[0], groups[1]
    local_groups, domain_groups = local_part.split('.'), domain_part.split('.')
    
    if not all(is_valid_group(group) for group in local_groups) or not all(is_valid_group(group) for group in domain_groups):
        print("Faillling....",local_groups,domain_groups)
        return 0

    results = []
    generate_emails(pattern, '', 0, results)
    return len(results)

# Example usage
pattern = "abcd@?bcd.ca"
print("count",solution(pattern))  # Output: 5
