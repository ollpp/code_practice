from collections import deque

def solution(number, k):

    # 문제를 이해하는게 가장 중요하다.
    # 가장 큰 조건 : 앞자리에 큰수가 올수록 전체가 커진다 -> 하나씩 넣을때 뒷자리가 더 크면 앞으로 뺀다.
    #           : 다만, k보다 더 빼면 안된다.
    # 주위할 점    : 만약 전체 number를 순회하였는데도 k 가 남아있다면 멈추지 말고 나머지 숫자도 모두 반영해준다. 
    
    number_q = deque(list(number))
    answer_list = []

    cnt = 0
    while number_q:

        temp = number_q.popleft()
        answer_list.append(temp)
        
        if cnt == k:
            pass
            
        else:
            while (cnt < k) and len(answer_list) > 1:
                if answer_list[-1] > answer_list[-2]:
                    answer_list.pop(-2)
                    cnt += 1
                else :
                    break

    if cnt != k:
        tmp = k - cnt
        answer_list = answer_list[:-tmp]


    
    answer=''.join(answer_list)
    return answer