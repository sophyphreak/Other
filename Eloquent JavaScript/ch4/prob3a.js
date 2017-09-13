// function arrayToList(arr) {
//   if (!arr) return null;
//   return {
//     value: arr.shift(),
//     rest: arrayToList(arr)
//   }
// }
// First try at arrayToList. didn't work because you
// can't test for an empty array that way.
// Must to length check as below.

function arrayToList(arr) {
  if (arr.length === 0) return null;
  return {
    value: arr.shift(),
    rest: arrayToList(arr)
  }
}

function listToArray(list) {
  if (!list.rest) return [list.value];
  return [list.value].concat(listToArray(list.rest));
}
