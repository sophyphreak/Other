
function getIndexToIns(arr, num) {
  arr.sort(function(a, b) {
    return a - b;
  });

  for (i = 0; i < arr.length; i++) {

    if (i == 0) {

      if (num <= arr[i]) {
        return 0;
      }
    }

    if (arr[i] == num) {
      return i;
    }

    if (arr[i] < num) {
      if (arr[i + 1] >= num) {
              console.log("got here")
        return i + 1
      }
    }
  } // end for loop

  return arr.length;
}
