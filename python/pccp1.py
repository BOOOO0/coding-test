def solution(bandage, health, attacks):
    t = attacks[len(attacks) - 1][0]
    health_limit = health
    flag = 0
    attacks_index = 0

    for i in range(1, t + 1):
        if i == attacks[attacks_index][0]:
            health = health - attacks[attacks_index][1]
            attacks_index = attacks_index + 1
            flag = 0
        else:
            health = health + bandage[1]
            if health > health_limit:
                health = health_limit
            flag = flag + 1

        if flag == bandage[0]:
            health = health + bandage[2]
            if health > health_limit:
                health = health_limit
            flag = 0

        if health < 1:
            return -1

    answer = health
    return answer
