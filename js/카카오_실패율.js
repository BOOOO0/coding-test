function solution(N, stages) {
  let answer = [];
  let map = new Map();
  for (let i = 0; i < N; i++) {
    let stage = i + 1;
    let total = 0;
    let fail = 0;
    for (let x of stages) {
      if (x > stage) {
        total++;
      } else if (x === stage) {
        fail++;
      }
    }
    map.set(stage, fail / total);
  }
  let sortedByValue = [...map].sort((a, b) => b[1] - a[1]);
  for (let i = 0; i < N; i++) {
    answer.push(sortedByValue[i][0]);
  }
  return answer;
}
