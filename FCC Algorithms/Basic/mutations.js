
function mutation(arr) {

  var long = arr[0].toLowerCase();
  var short = arr[1].toLowerCase();

  for (i=0; i < short.length; i++) {
    if (long.indexOf(short[i]) == -1) {
      console.log(i)
      return false;
    }
  }
  return true;
}

console.log(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]));
