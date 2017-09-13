var board = "";
var size = 8;
var hash = false;

for (var i = 0; i < size; i++) {
  for (var j = 0; j < size; j++) {
    if (hash) {
      board += "#";
      hash = !hash;
    } else {
      board += " ";
      hash = !hash;
    }
    if (j === size - 1) {
      board += "\n";
      hash = !hash;
    }
  }
}

console.log(board);
