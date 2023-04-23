// n-튜플들이 문자열로 주어지고
// 그 n-튜플을 바탕으로 튜플을 유추해내는 문제이다

function solution(s) {
  let answer = [];
  let arr = s
    .slice(2, -2)
    .split("},{")
    .map((elm) => elm.split(","))
    .sort((a, b) => a.length - b.length);
  // 순회 방법
  // 우선 이중포문으로 하나씩 순회하면서 포함되지 않은 원소들을 answer에 push

  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < arr[i].length; j++) {
      if (!answer.includes(arr[i][j])) {
        answer.push(arr[i][j]);
      }
    }
  }
  return answer.map((elm) => parseInt(elm));
}
