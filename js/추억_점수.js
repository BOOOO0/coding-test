let names = ["may", "kein", "kain", "radi"];
let yearning = [5, 10, 1, 3];
let photo = [
  ["may", "kein", "kain", "radi"],
  ["may", "kein", "brin", "deny"],
  ["kon", "kain", "may", "coni"],
];
function calculation(nameMap, photo) {
  let sum = 0;
  console.log(photo);
  photo.forEach((e) => {
    isNaN(nameMap.get(e)) ? (sum += 0) : (sum += nameMap.get(e));
  });

  return sum;
}
function solution(name, yearning, photo) {
  var answer = [];
  let nameMap = new Map();

  name.forEach((e, i) => {
    nameMap.set(e, yearning[i]);
  });

  while (photo.length > 0) {
    answer.push(calculation(nameMap, photo.shift()));
  }

  return answer;
}
console.log(solution(names, yearning, photo));
