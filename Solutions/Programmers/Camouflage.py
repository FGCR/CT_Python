import copy

answer = 0
def solution(clothes):
    cloth_dict = dict()
    for i in range(len(clothes)):
        key = clothes[i][1]
        value = clothes[i][0]
        if not (key in cloth_dict):
            cloth_dict[key] = list()
        cloth_dict[key].append(value)

    def dressing(left_clothes: dict):
        global answer
        for Cloth_Type in list(left_clothes.keys()):
            for i in range(left_clothes[Cloth_Type]):
                cloth
                now_left_clothes = copy.deepcopy(left_clothes)
                now_left_clothes[Cloth_Type].remove(cloth)
                answer += 1
                dressing(now_left_clothes)

    dressing(cloth_dict)

    return answer

print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))