import sys
inputf = sys.stdin.readline

S = list(inputf().rstrip())
ord_range = [(97,123),(65,91)]

for i,s in enumerate(S):
    if s.isalpha():
        ord_s = ord(s)
        if 97<=ord_s<123:
            if ord_s+13>=123:
                S[i] = chr(ord_s+13-123+97)
            else:
                S[i] = chr(ord_s+13)
        else:
            if ord_s+13>=91:
                S[i] = chr(ord_s+13-91+65)
            else:
                S[i] = chr(ord_s+13)

print(''.join(S))