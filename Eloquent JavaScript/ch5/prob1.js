// input: array of arrays
// returns: "flattened" array

var arrays = [[1, 2, 3], [4, 5], [6]];

console.log(flattening(arrays));

function flattening(arr) {
  return arr.reduce(function(result, value) {
    return result.concat(value);
  }, []);
}
