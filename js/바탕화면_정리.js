function solution(wallpaper) {
  var answer = [];
  let column = 0;
  let min = [Number.MAX_SAFE_INTEGER, Number.MAX_SAFE_INTEGER];
  let max = [Number.MIN_SAFE_INTEGER, Number.MIN_SAFE_INTEGER];
  for (let x of wallpaper) {
    for (let i = 0; i < x.length; i++) {
      if (x[i] === "#") {
        min = [Math.min(min[0], column), Math.min(min[1], i)];
        max = [Math.max(max[0], column + 1), Math.max(max[1], i + 1)];
      }
    }
    column++;
  }

  return [...min, ...max];
}
