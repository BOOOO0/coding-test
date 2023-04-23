function solution(board, moves) {
  var answer = 0;
  let stk = [];

  for (let x of moves) {
    for (let i = 0; i < board.length; i++) {
      if (board[i][x - 1] !== 0) {
        if (stk.length === 0) {
          stk.push(board[i][x - 1]);
          board[i][x - 1] = 0;
          break;
        } else if (stk[stk.length - 1] === board[i][x - 1]) {
          stk.pop();
          board[i][x - 1] = 0;
          answer += 2;
          break;
        } else {
          stk.push(board[i][x - 1]);
          board[i][x - 1] = 0;
          break;
        }
      }
    }
  }
  return answer;
}
