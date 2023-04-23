function mapping() {
  let map = new Map();
  map.set("zero", "0");
  map.set("one", "1");
  map.set("two", "2");
  map.set("three", "3");
  map.set("four", "4");
  map.set("five", "5");
  map.set("six", "6");
  map.set("seven", "7");
  map.set("eight", "8");
  map.set("nine", "9");
  return map;
}
function solution(s) {
  let answer = "";
  let map = mapping();

  let word = "";

  for (let x of s) {
    if (!isNaN(x)) {
      answer += x;
    } else {
      word += x;
      if (map.has(word)) {
        answer += map.get(word);
        word = "";
      }
    }
  }
  return Number(answer);
}
