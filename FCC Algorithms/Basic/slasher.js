function slasher(arr, howMany) {
  if (arr.length < howMany) {
    return [];
  }
  arr = arr.slice(howMany);
  return arr;
}

console.log(slasher([1, 2, 3], 2));
