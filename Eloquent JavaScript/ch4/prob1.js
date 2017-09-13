// function range(a, b) {
//   var ansArr = [];
//   for (var i = a; i <= b; i++) {
//     ansArr.push(i);
//   }
//   return ansArr;
// }

function sum(arr) {
  var sum = 0;
  for (var i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}

function range(a, b, c) {
  var ansArr  = [];
  if (!c) c = 1;
  if (c > 0) {
    for (var i = a; i <= b; i += c) {
      ansArr.push(i);
    }
  } else {
    for (var i = a; i >= b; i += c) {
      ansArr.push(i);
    }
  }
  return ansArr;
}
