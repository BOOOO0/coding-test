// S = [0,0]
// SOO
// OOO
// OOO
// E 일 경우 S[0] += 1
// E,2 면 [2,0]

function solution(park, routes) {
  var answer = [];
  let row, column;
  park.forEach((e, i) => {
    if (e.includes("S")) {
      column = i;
      row = e.indexOf("S");
    }
  });
  while (routes.length > 0) {
    let [direction, distance] = routes.shift().split(" ");
    let flag = true;
    let tempRow = row;
    let tempColumn = column;
    for (let i = 0; i < distance; i++) {
      switch (direction) {
        case "E":
          tempRow++;
          break;
        case "W":
          tempRow--;
          break;
        case "S":
          tempColumn++;
          break;
        case "N":
          tempColumn--;
          break;
      }
      if (
        tempRow >= park[0].length ||
        tempColumn >= park.length ||
        tempRow < 0 ||
        tempColumn < 0 ||
        park[tempColumn][tempRow] === "X"
      ) {
        flag = false;
        break;
      }
    }
    if (flag) {
      row = tempRow;
      column = tempColumn;
    }
  }

  return [column, row];
}
