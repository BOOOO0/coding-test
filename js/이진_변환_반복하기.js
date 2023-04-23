function solution(s) {
  var answer = [];

  let ones = "";
  let zero_result = 0;
  let result = 0;

  while (s.length != 1) {
    let arr = s.split("");
    let ones = [];
    let zeros = 0;
    for (let x of arr) {
      if (x == 1) ones.push(x);
      else zeros++;
    }
    result++;
    zero_result += zeros;
    s = ones.length.toString(2);
  }

  return [result, zero_result];
}
