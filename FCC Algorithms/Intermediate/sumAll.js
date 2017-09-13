
function sumAll(arr) {
  var x = arr[0];
  var y = arr[1];
  if (x > y) {
    [x, y] = [y, x]; //Now x is smaller than y
  }

  var sum = 0;
  for(i = x; i <= y; i++) {
    sum += i;
  }

  return sum;
}

console.log(sumAll([1, 4]));
