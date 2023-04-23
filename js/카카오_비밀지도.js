function binary(n, arr) {
  let board = [];
  let bin = "";
  for (let x of arr) {
    bin = "";
    if (x.toString(2).length < n) {
      bin = x.toString(2);
      for (let i = 0; i < n - x.toString(2).length; i++) {
        bin = "0" + bin;
      }
      board.push(bin);
    } else {
      board.push(x.toString(2));
    }
  }
  return board;
}
function solution(n, arr1, arr2) {
  var answer = [];
  let board1;
  let board2;
  board1 = binary(n, arr1);
  board2 = binary(n, arr2);

  let pt1, pt2;
  let code;
  for (let i = 0; i < n; i++) {
    code = "";
    for (let j = 0; j < n; j++) {
      pt1 = board1[i][j];
      pt2 = board2[i][j];

      if (pt1 == 0 && pt2 == 0) {
        code += " ";
      } else {
        code += "#";
      }
    }
    answer.push(code);
  }

  return answer;
}
