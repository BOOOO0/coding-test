function solution(s) {
  // 원형큐라고 생각을하고
  // 우선 길이만큼 회전을 시키는데
  // 회전 시키는 동안 올바른 괄호 문자열의 수를 구하는 문제
  // 올바른 문자열인지 검사하는 로직이 필요한데
  // 실제로 회전을 시키지말고
  // 길이가 6이라면 0부터 1 0부터 2 0부터3 이렇게 5까지 검사를 진행

  var answer = 0;
  let bool = true;
  let stk = [];
  // s의 길이가 홀수라면 return 0;
  if (s.length % 2 === 1) return 0;
  for (let i = 0; i < s.length; i++) {
    // 인덱스 하나는 그만큼을 0부터 짜른 후 나머지
    // 인덱스 두개는 strat 부터 end 까지 만큼을 반환
    // 나머지 + 추출된 문자열 = 회전이라고 볼 수 있다
    let candidate = s.slice(i) + s.slice(0, i);
    bool = true;
    for (let x of candidate) {
      if (x === "(" || x === "{" || x === "[") stk.push(x);
      else {
        if (x === ")" && stk.pop() === "(") continue;
        if (x === "}" && stk.pop() === "{") continue;
        if (x === "]" && stk.pop() === "[") continue;
        bool = false;
        break;
      }
    }
    if (bool) answer++;
  }

  return answer;
}
