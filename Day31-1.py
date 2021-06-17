#スタッククイズ -> 電話番号のメモニック表記
from typing import List

NUM_ALPHABET_MAPPING = {
    0: '+',
    1: '@',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ'
}

def phone_mnemonic_v1(phone_numbers : str ) -> List[str]:
    phone_numbers =[int(s) for s in phone_numbers.replace('-', '')]
    candidate = []
    tmp = [''] * len(phone_numbers)
    def find_cadidate(didit:int=0 ) -> None:
        if didit == len(phone_numbers):
            candidate.append(''.join(tmp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_numbers[didit]]:
                tmp[didit] = char
                find_cadidate(didit + 1)
    find_cadidate()
    return candidate



def phone_mnemonic_v2(phone_numbers : str ) -> List[str]:
    phone_numbers =[int(s) for s in phone_numbers.replace('-', '')]
    candidate = []
    stack = ['']
    while len(stack) != 0:
        alphabets = stack.pop()
        if len(alphabets) == len(phone_numbers):
            candidate.append(alphabets)
        else:
            for char in NUM_ALPHABET_MAPPING[phone_numbers[len(alphabets)]]:
                stack.append(alphabets + char)
    return candidate



if __name__ == "__main__":
    for s in phone_mnemonic_v2('568-379-8466'):
        if 'LOVEPYTHON' in s:
            print(s)


