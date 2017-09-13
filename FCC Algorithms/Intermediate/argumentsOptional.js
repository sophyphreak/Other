function addTogether(a,b) {

  if (arguments.length === 1 && typeof(a) === 'number') {
    return function(b2) {
      if (typeof(a) != 'number' || typeof(b2) != 'number') {
        return undefined;
      }
      return a + b2;
    };
  }

  if (typeof(a) != 'number' || typeof(b) != 'number') {
    return undefined;
  }


  return a + b;
}

console.log(
  addTogether(2,3),
  addTogether(2)(3),
  addTogether("http://bit.ly/IqT6zt"),
  addTogether(2)([3])
);
