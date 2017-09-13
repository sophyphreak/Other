for (var count = 1; count < 101; count++) {
  if (count % 15 === 0) console.log("fizzbuzz");
  else if (count % 3 === 0) console.log("fizz");
  else if (count % 5 === 0) console.log("buzz");
  else console.log(count);
}
