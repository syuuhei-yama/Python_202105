#Palindrome
# s = "test"
# # tesprint(s == ''.join(reversed(s)))
#
# print(s == s[::1])

def is_palindrome(string : str) -> bool:
    len_strings = len(string)
    if not len_strings:
        return False
    if len_strings == 1:
        return True


    start, end = 0, len_strings -1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True



def find_palindrome(strings: str, left: int ,right: int):
    result = []
    while 0 < left and right <= len(strings) -1:
        if strings[left] != strings[right]:
            break
        result.append(strings[left: right+1])
        left -= 1
        right += 1
    return result

def find_all_palindrome(strings : str):
    result = []
    len_string = len(strings)
    if not len_string:
        return result
    if len_string == 1:
        result.append(strings)

    for i in range(1, len_string-1):
        [result.append(s) for s in find_palindrome(strings, i - 1, i + 1)]
        [result.append(s) for s in find_palindrome(strings, i - 1, i)]

    return result



if __name__ == "__main__":
    # print(find_palindrome("cabac",1, 3))
    # print(find_palindrome("cabbac",2, 3))
    # print(is_palindrome('test'))
    print(find_all_palindrome("cabac"))