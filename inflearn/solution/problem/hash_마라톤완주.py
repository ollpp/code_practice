# hash 를 사용하여
# 문자열을 인덱스로 활용하여 접근한다.
# key : 사람들의 이름

def solution(participant, completion):
    d = {}

    for x in participant:
        # .get : x key값이 있으면 value를, 없으면 0을 가져온다.
        d[x] = d.get(x, 0) + 1

    for x i n completion:
        d[x] -= 1

    dnf = [k for k, v in d.items() if v>0]

    answer = dnf[0]

    return answer