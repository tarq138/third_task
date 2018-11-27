
def sol(S):
    S += '\n'
    left = 0
    ans = 0
    while S.find('\n') != -1:
        number = S[S.find(',')+1:S.find('\n')]
        hh = int(S[0:S.find(':')])
        S = S[S.find(':')+1:len(S)]
        mm = int(S[0:S.find(':')])
        S = S[S.find(':')+1:len(S)]
        ss = int(S[0:S.find(',')])
        S = S[S.find('\n')+1:len(S)]
        s = hh*3600+mm*60+ss;
        if s < 300:
            pay = s * 3
        else:
            mm = mm + 60 * hh
            if ss > 0:
                mm += 1
            pay = mm * 150
        if pay > ans:
            ans = pay
    return(ans)

print(sol('00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'))
