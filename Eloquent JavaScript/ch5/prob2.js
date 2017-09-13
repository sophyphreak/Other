var ancestry = JSON.parse(require("./ancestry.js"));

// function average(array) {
//   function plus(a, b) { return a + b; }
//   return array.reduce(plus) / array.length;
// }

var byName = {};
ancestry.forEach(function(person) {
  byName[person.name] = person;
});

function ageDifference(child, mother) {
  console.log(child["name"], mother["name"]);
  return mother["born"] - child["born"];
}

function hasMotherObject(motherName) {
  return !!byName[motherName];
}

function averageAgeDifference(byName) {
  var differencesArray = Object.keys(byName).reduce(function(accum, current) {
    if (/*hasMotherObject(byName[current["mother"]])*/ true) {
      accum.concat(
        ageDifference(
          byName[current],
          byName[byName[current["mother"]]]
        )
      );
    }
    return accum;
  }, []);
  // return average(differencesArray);
  return differencesArray;
}

console.log(averageAgeDifference(byName));

// Your code here.

// → 31.2
