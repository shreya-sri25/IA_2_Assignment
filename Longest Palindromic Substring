def longest_palindrome(s):
    if not s:
        return ""

    start = end = 0

    for i in range(len(s)):
        len1 = expand_center(s, i, i)     # Odd length
        len2 = expand_center(s, i, i + 1) # Even length
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def expand_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

if __name__ == "__main__":
    s = "babad"
    print("Longest Palindromic Substring:", longest_palindrome(s))
