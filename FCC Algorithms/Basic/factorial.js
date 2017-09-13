// noprotect
function factorialize(num) {
  if(num == 0){
    return 1;
  }
  var max = num;
  for(i = 1; i < max; i++) {
    num *= i;
  }

  return num;
}

factorialize(5);
