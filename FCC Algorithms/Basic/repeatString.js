
function repeatStringNumTimes(str, num) {

  var result = "";

  for(i = 0; i < num; i++){
    result += str;
  }

  return result;
}

console.log(repeatStringNumTimes("abc", 3));
