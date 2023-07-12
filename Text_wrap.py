import textwrap

def wrap(string, max_width):
    # used textwrap library 
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)






    
# def wrap(string, max_width):
#     s = []
#     for i in range(0, len(string), max_width):
#         s.append( string[i:i+max_width])
#     for x in s:
#         print(x)

#         # print(s)
#     return s

