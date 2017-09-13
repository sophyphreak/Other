
function dropElements(arr, func) {

  let resArr = arr.slice();

  for (i = 0; i < arr.length; i++) {
    if (func(resArr[0]) == true) {
      return resArr;
    } else {
      resArr.shift();
    }
  }

  return resArr;
}
console.log(
  dropElements([1, 2, 3, 4], function(n) {return n > 5;})
);
