def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # backtrack
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0  # i for text, j for pattern

    print(f"Searching for '{pattern}' in '{text}'")
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]  # Continue searching
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  # Try previous match
            else:
                i += 1
