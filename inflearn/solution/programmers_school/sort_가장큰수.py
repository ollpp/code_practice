def solution(numbers):

    str_numbers = [str(x) for x in numbers]
    
    # 주어진 x를 정렬하는 기준을 세워준다.
    # x의 경우 특정 자릿수까지 같을 경우, 해당 x가 가질 수 있는 최대숫자의 경우를 만들고,
    # 이를 크기 비교하여 sort 시켜준다.
    # 기준의 경우 sort 문제 조건이 1000 이하이기때문에 4로 걸어준다.
    str_numbers.sort(key=lambda x : (x*4)[:4], reverse = True)

    if str_numbers[0] == '0':
        answer = '0'
    else :
        answer = ''.join(str_numbers)


    return answer
