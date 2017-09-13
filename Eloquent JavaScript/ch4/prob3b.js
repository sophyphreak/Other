function prepend(el, list) {
  return {value: el, rest: list};
}

function nth(list, number) {
  if (!list.rest) return undefined;
  if (number === 0) return list.value;
  return nth(list.rest, number - 1);
}

// function arrayToList(arr) {
//   var list = null;
//   for (var i = 0; i < arr.length; i++) {
//     list = prepend(arr[arr.length - 1 - i], list); // initially had a problem going from 1st to last val in arr instead of last to 1st
//   }
//   return list;
// }

// I decided to rewrite arrayToList as a pretty recursive function because I can.
function arrayToList(arr) {
  if (arr.length === 0) return null;
  return prepend(arr.shift(), arrayToList(arr));
}

function listtoArray(list) {
  var arr = [], index = 0;
  while (true) {
    var val = nth(list, index);
    if (val) {
      arr.push(val);
      index++;
    } else break;
  }
  return arr;
}
