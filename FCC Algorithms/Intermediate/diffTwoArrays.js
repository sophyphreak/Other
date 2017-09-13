
function diffArray(arr1, arr2) {
  var newArr = [];

  var bothArr = arr1.concat(arr2);
  //console.log(bothArr);
  var result = [];

  for (i = 0; i < bothArr.length; i++) {
    //console.log("i=", i, bothArr[i]);
    var arr1Has = arr1.indexOf(bothArr[i]);
    var arr2Has = arr2.indexOf(bothArr[i]);

    //console.log(i, bothArr[i], arr1Has, arr2Has);

    if (( arr1Has > -1 || arr2Has > -1 ) && !( arr1Has > -1 && arr2Has > -1 )) {
      //console.log([bothArr[i]]);
      result.push(bothArr[i]);
    }
  }
  return result;
}

console.log(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]));
