
function sumPrimes(num) {

  let primeArr = [2];
  let cur;


  while (0 != 1) {
    cur = primeArr[primeArr.length - 1];
    while (cur <= num) {
      cur += 1;
      for (i = 2; i < cur; i++) {
        if (cur % i === 0) {
          break;
        }
        if (i === cur - 1) {
          primeArr.push(cur);
        }
      }
    }

    if (primeArr[primeArr.length - 1] >= num) {
      break;
    }
  }

  if (primeArr[primeArr.length - 1] != num) {
  return primeArr.slice(0, primeArr.length - 1).reduce(function(sum, value){
    return sum + value;
  }, 0);
} else {
  return primeArr.reduce(function(sum, value){
    return sum + value;
  }, 0);
}
}

console.log(
  sumPrimes(977)
);
