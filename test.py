class Palindrome:
    @staticmethod
    def is_palindrome(word):
        return word.lower()


word = input()
print(Palindrome.is_palindrome(word))



def findChar(array):
    arr_len = len(array)
    if arr_len == 0:
        return
    dict = {}
    re_arr = []
    for i in array:
        if i in dict.keys():
            dict[i] += 1
            if dict[i] > arr_len/2:
                re_arr.append(i)
        else:
            dict[i] = 1
    return re_arr
