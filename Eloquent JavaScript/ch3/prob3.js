function countBs (str) {
  var bCount = 0;
  for (var i = 0; i < str.length; i++) {
    if (str.charAt(i) === "B") bCount++;
  }
  return bCount;
}

function countChar(str, char) {
  var charCount = 0;
  for (var i = 0; i < str.length; i++) {
    if (str.charAt(i) === char) charCount++;
  }
  return charCount;
}
