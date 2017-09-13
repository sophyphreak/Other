
function confirmEnding(str, target) {
  // "Never give up and good luck will find you."
  // -- Falcor

  return target == str.substring(str.length - target.length);

}

console.log(confirmEnding("Bastian", "n"));
