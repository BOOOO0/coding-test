def solution(s):
    answer = []

    dic = dict()

    for i in range(len(s)):
        if s[i] not in dic:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        # 없을 경우에는 딕셔너리에 문자, 그 문자의 현 인덱스 등록
        # 있을 경우엔 문자의 최신 인덱스 갱신
        dic[s[i]] = i

    return answer
