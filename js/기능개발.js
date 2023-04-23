// progress 에 speed를 더해주는데
// 모든 progress에 동시에 자기 인덱스의 speed를 더해준다
// 100 이상이 된 progress들의 수를 answer에 push  filter로 100이상된 progress 배열 새로 할당하고 그 배열의 길이
// progress의 index 순서에 따라서 배포가 결정된다
// 앞에 놈이 안끝나면 더 나중에 간다
// 그럼 앞에 놈이 스택 맨 끝이고
// progress에 speed 더하는 연산 진행
// 조건문으로 [0] 이 100 이상인지 확인
// 이상이면 pop 시키면서 몇번 pop 되었는지를 answer에 push
// 0번이 0이면 배열 전체를 순회하면서 cnt 세는 함수

function solution(progresses, speeds) {
  var answer = [];
  let days = 1;
  let cnt = 0;
  while (progresses.length !== 0) {
    let progress = progresses[0] + speeds[0] * days;
    if (progress >= 100) {
      progresses.shift();
      speeds.shift();
      cnt++;
      console.log(progresses, cnt);
    } else {
      if (cnt > 0) {
        answer.push(cnt);
      }
      cnt = 0;
      days++;
    }
  }

  answer.push(cnt);
  return answer;
}
