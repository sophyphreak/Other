function reverseArray(arr) {
  var newArr = [];
  for (var i = 0; i < arr.length; i++) {
    newArr.push(arr[arr.length - 1 - i]);
  }
  return newArr;
}

function reverseArrayInPlace(arr) {
  var newArr = [];
  var arrLength = arr.length;
  for (var i = 0; i < arrLength; i++) {
    newArr.push(arr.pop());
  }
  for (var i = 0; i < arrLength; i++) {
    arr.push(newArr.shift());
  }
}
