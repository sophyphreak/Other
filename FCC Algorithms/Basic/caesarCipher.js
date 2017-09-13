
function rot13(str) { // LBH QVQ VG!

  var rot13 = {
    "A":"N",
    "B":"O",
    "C":"P",
    "D":"Q",
    "E":"R",
    "F":"S",
    "G":"T",
    "H":"U",
    "I":"V",
    "J":"W",
    "K":"X",
    "L":"Y",
    "M":"Z",
    "N":"A",
    "O":"B",
    "P":"C",
    "Q":"D",
    "R":"E",
    "S":"F",
    "T":"G",
    "U":"H",
    "V":"I",
    "W":"J",
    "X":"K",
    "Y":"L",
    "Z":"M"
  };

  var result = "";

  for (i = 0; i < str.length; i++) {
    var alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNM";
    if (alphabet.indexOf(str[i]) == -1) {
      result += str[i];
    } else {
      result += rot13[str[i]];
    }
  }

  return result;
}

// Change the inputs below to test
console.log(rot13("SERR PBQR PNZC"));
