from collections import defaultdict

id_list = ["muzi", "frodo", "apeach", "neo"]

report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

k = 2

answer = [0 for _ in range(len(id_list))]

report = set(report)
# 한 사람이 여러명을 신고할 수 있다
# 하지만 같은 사람을 여러번 신고할 수는 없다

who = defaultdict(set)
what_times = defaultdict(int)
banned = []

for r in report:
    report_want , reported = map(str,r.split())

    what_times[reported] += 1
    who[report_want].add(reported)
    
    if what_times[reported] == k:
        banned.append(reported)

for b in banned:
    for i in range(len(id_list)):
        # i 인덱스 이용해서 id_list에 이름에 해당하는 인덱스의 DP를 +1 시킨다
        if b in who[id_list[i]]:
            answer[i] += 1
            
print(answer)
    
    