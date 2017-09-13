
function bouncer(arr) {
  arr = arr.filter(function(val){
    var badVal = [false, null, 0, "", undefined];
    return !(badVal.indexOf(val) > -1 || (isNaN(val) && typeof(val) != "string"));

  });
  return arr;
}

// Everything below was just for testing


var ex = [
  [7, "ate", "", false, 9],
  ["a", "b", "c"],
  [false, null, 0, NaN, undefined, ""],
  [1, null, NaN, 2, undefined]
]

for (i = 0; i < ex.length; i++) {
  console.log(bouncer(ex[i]))
}
