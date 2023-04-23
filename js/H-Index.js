function solution(citations) {
  var answer = 0;
  citations.sort((a, b) => b - a);
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] > i) answer++;
  }
  // h는 citation의 원소를 말하는 것이 아니라
  // 최댓값을 구한 것이 h이다.
  return answer;
}
