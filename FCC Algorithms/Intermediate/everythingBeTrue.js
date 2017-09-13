
function truthCheck(collection, pre) {
  for (let obj in collection) {
    if (Boolean(collection[obj][pre]) == false) {
      return false;
    }
  }
  return true;
}


console.log(
truthCheck([{"user": "Tinky-Winky", "sex": "male"}, {"user": "Dipsy", "sex": "male"}, {"user": "Laa-Laa", "sex": "female"}, {"user": "Po", "sex": "female"}], "sex")
);
