

function destroyer(arr) {
  var toDestroy = Array.from(arguments);
  var pool = toDestroy.shift();
  return pool.filter(function(val){
    return toDestroy.indexOf(val) == -1;
  });
}

console.log(destroyer([1, 2, 3, 1, 2, 3], 2, 3));
