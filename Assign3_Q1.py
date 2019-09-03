def revAlternateK(s, k, Len):
    i = 0

    while (i < len(s)):

        if (i + k > Len):
            break


        ss = s[i:i + k]
        s = s[:i] + ss[::-1] + s[i + k:]
        i += 2 * k

    return s;


s = "sriharshini"
Len = len(s)
k = 2
print(revAlternateK(s, k, Len))
