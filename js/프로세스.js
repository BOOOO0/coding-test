// 값으로 검색 x

function solution(priorities, location) {
  var answer = 0;

  while (1) {
    let max = Math.max(...priorities);
    let zero = priorities.shift();
    if (zero === max) {
      answer++;
      if (location === 0) {
        break;
      }
    } else {
      priorities.push(zero);
    }
    location--;
    if (location < 0) location = priorities.length - 1;
  }
  return answer;
}
