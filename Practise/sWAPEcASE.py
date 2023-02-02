from ntpath import join


def swap_case(s):
    cst_s = list(s)
    for i in range(len(s)) :
        if(s[i].isupper()):
            cst_s[i] = cst_s[i].lower()
        else:
            cst_s[i] = cst_s[i].upper()
    
    return ''.join(cst_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)