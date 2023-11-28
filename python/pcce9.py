def validation(n, h, w, dh, dw):
    if h + dh == n or h + dh < 0:
        return False
    if w + dw == n or w + dw < 0:
        return False
    return True


def check(hw_color, other_color):
    if hw_color == other_color:
        return True
    return False


def solution(board, h, w):
    answer = 0
    n = len(board[0])

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(0, 4):
        if validation(n, h, w, dh[i], dw[i]):
            if check(board[h][w], board[dh[i] + h][dw[i] + w]):
                answer = answer + 1

    return answer
