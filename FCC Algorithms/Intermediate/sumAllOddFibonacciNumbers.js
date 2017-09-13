function sumFibs(num) {

  let fib = [1, 1];

  for (i = 0; i < 50; i++) {
    fib.push(
      fib[fib.length - 1] + fib[fib.length - 2]
    );
  }

  fib = fib.filter((val) => val % 2 === 1);
  fib = fib.filter((val) => val <= num);
  let result = fib.reduce(function(sum, value) {
    return sum + value;
  });

  return result;
}
console.log(
  sumFibs(4)
);
