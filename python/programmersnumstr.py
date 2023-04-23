
def solution(s):
    answer = ""
    num_str = {"zero" : "0","one": "1" , "two":"2" , "three":"3" , "four":"4" , "five":"5" , "six":"6", "seven" :"7",
               "eight":"8", "nine":"9"}
    num = ""
    for char in s:
        if char.isdigit():
            answer += char
        else:
            num += char
            if num in num_str:
                answer += num_str[num]
                num = ""
    
    return int(answer)

print(solution("one4seveneight"))