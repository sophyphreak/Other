function steamrollArray(arr) {

  let hasInnerArray = true;

  while (hasInnerArray == true) {

    arr = arr.reduce(function(a, b) {
      return a.concat(b);
    }, []);

    hasInnerArray = false;

    for (let index in arr) {
      if (Array.isArray(arr[index])) {
        hasInnerArray = true;
      }
    }

  }

  return arr;
}
console.log(
  steamrollArray([1, [2], [3, [[4]]]])
);
