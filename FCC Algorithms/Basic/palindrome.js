function palindrome(str) {

  var onlyLetters = str.match(/[a-zA-Z0-9]+/g).join("").toLowerCase();

  var max = Math.floor(onlyLetters.length/2);

  for (i = 0; i < max; i++){
    if (onlyLetters[i] != onlyLetters[onlyLetters.length-1-i]) {
      return false;
    }
  }

  return true;
}

// For eac


console.log(palindrome("2_A3*3#A2"));
