
function translatePigLatin(str) {

  let staticArr = str.split("");
  let flexArr = staticArr.slice();
  let tempChar = ""

  for (index = 0; index < staticArr.length; index++) {
    if ("aeiou".indexOf(staticArr[index]) == -1) {
      tempChar = flexArr.shift();
      flexArr.push(tempChar);
    } else {
      if (index == 0) {
        flexArr.push("w");
      }
      break;
    }
  }

  flexArr.push("ay");
  str = flexArr.join("");

  return str;
}
console.log(
  translatePigLatin("algorithm")
);
