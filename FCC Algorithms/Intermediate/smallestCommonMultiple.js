
function smallestCommons(arr) {
  let lower = Math.min(arr[0], arr[1]);
  let upper = Math.max(arr[0], arr[1]);
  let factorString = [];

  for (i = lower; i <= upper; i++) {
    factorString.push(i);
  }

  let cur = 1;
  let flag = false;

  while (0 != 1) {
    cur++;
    if (cur == 9999999) {break;}
    for (let index in factorString) {
      if (cur % factorString[index] != 0) {
        flag = true;
        break;
      }
    }
    if (flag === true) {
      flag = false;
      continue;
    } else {
      return cur;
    }
  }
}

console.log(
  smallestCommons([1, 5]), '\n',
  smallestCommons([5, 1]), '\n',
  smallestCommons([23, 18])
);
