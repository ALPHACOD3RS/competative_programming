# def isAnagram(a: str, b: str) -> bool:
#     if len(a) == len(b):
#         for i in range(len(a)):

#             if a[i]not in b :
#                 return False
#         return True
#     else:
#         return False
def isAnagram(s: str, t: str) -> bool:
    x = sorted(s)
    y = sorted(t)

    b = x == y

    return b
    

a = "aasd"
b= "asda"

print(isAnagram(a,b))