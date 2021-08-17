def solution(phone_book):
    answer = True

    phone_book = sorted(phone_book, key = len)
    phone_dict = dict()

    for phone_num in phone_book:
        for key in [item for item in list(phone_dict.keys()) if phone_num[0] == item[0]][::-1]:
            if len(key) > len(phone_num) and key[:len(phone_num)] == phone_num:
                return False
            elif len(phone_num) > len(key) and phone_num[:len(key)] == key:
                return False
        phone_dict[phone_num] = True

    return True

print(solution(["119", "97674223", "1195524421"]))