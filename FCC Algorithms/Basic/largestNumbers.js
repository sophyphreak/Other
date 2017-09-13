function largestOfFour(arr) {

  var result = [];

  for (i = 0; i < arr.length; i++) {
    var largest = 0;

    for (j = 0; j < 4; j++) {
      if (arr[i][j] > largest) {
        largest = arr[i][j];
      }
    }

    result.push(largest);
  }

  return result;
}

console.log(largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]));
