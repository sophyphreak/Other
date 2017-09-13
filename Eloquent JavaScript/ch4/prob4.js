// function deepEqual (a, b) {
//   if (typeof(a) !== "object" || typeof(b) !== "object") return a === b;
//
//   for (var i in a) {
//     for (var j in b) {
//       if (!deepEqual(a[i], b[j])) return false;
//     }
//   }
//   return true;
// } // original, incorrect version
// forgot how to loop through correctly

function deepEqual (a, b) {
  if (typeof(a) !== "object" || typeof(b) !== "object") return a === b;

  for (var i in a) {
    if (!deepEqual(a[i], b[i])) return false;
  }
  return true;
}
