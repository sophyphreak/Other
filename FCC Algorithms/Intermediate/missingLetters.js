
function fearNotLetter(str) {
  let arr = str.split("");
  let alphabetString = "abcdefghijklmnopqrstuvwxyz";
  let alphaSplit = alphabetString.split("");
  let alpha = alphaSplit.slice(0, arr.length);

  if (arr[0] != 'a') {
    return undefined;
  }

  for (var index in arr) {
    if (arr[index] != alpha[index]) {
      return alpha[index];
    }
  }

  return "Got here";
}

fearNotLetter("abce");
