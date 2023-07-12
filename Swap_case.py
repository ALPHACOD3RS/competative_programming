def swap_case(s):
    z = []
    k = ''
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].islower():
                # print("uu")
                z.append(s[i].upper())
            else:
                z.append(s[i].lower())
            # print("asdfhas")
        else:
            z.append(s[i])

    k = ''.join(x for x in z)


    
    return k



if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)