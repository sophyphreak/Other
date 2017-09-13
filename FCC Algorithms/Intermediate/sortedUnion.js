function uniteUnique(arr) {

  arr = [].slice.call(arguments);

  arr = arr.reduce(( acc, cur ) => acc.concat(cur), []);

  let answer = [];

  for (let index in arr) {
    if (answer.indexOf(arr[index]) == -1) {
      answer.push(arr[index]);
    }
  }

  return answer;
}

console.log(
    uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1])
);
