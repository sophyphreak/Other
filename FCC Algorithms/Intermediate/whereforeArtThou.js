
function whatIsInAName(collection, source) {
  // What's in a name?
  var arr = [];
  // Only change code below this line

  let sourceKeys = Object.keys(source);
  let booleanAnswerList = [];
  for (i = 0; i < collection.length; i++) {
    booleanAnswerList.push(true);
  }
  // console.log(booleanAnswerList);
  for (i = 0; i < collection.length; i++) {
    let obj = collection[i];
    let objKeys = Object.keys(obj);
    for (index in sourceKeys) {
      if (objKeys.indexOf(sourceKeys[index]) === -1) {
          booleanAnswerList[i] = false;
          // console.log(objKeys, sourceKeys[index]);
      }
    }
    // console.log(booleanAnswerList);
    if (booleanAnswerList[i] === true) {
      for (var index in sourceKeys) {
        if (source[sourceKeys[index]] != obj[sourceKeys[index]]) {
          booleanAnswerList[i] = false;
        }
      }
    }
  }
  // console.log(booleanAnswerList);
  for (i = 0; i < collection.length; i++) {
    if (booleanAnswerList[i] === true) {
      arr.push(collection[i]);
    }
  }

  // Only change code above this line
  return arr;
}


let test = [
  whatIsInAName(
    [
      { first: "Romeo", last: "Montague" },
      { first: "Mercutio", last: null },
      { first: "Tybalt", last: "Capulet" }
    ],
    { last: "Capulet" }
  ),

  whatIsInAName(
    [
      { "a": 1 },
      { "a": 1 },
      { "a": 1, "b": 2 }
    ],
    { "a": 1 }
  ),
  whatIsInAName(
    [
      { "a": 1, "b": 2 },
      { "a": 1 },
      { "a": 1, "b": 2, "c": 2 }
    ],
    { "a": 1, "b": 2 }
  ),
  whatIsInAName(
    [
      { "a": 1, "b": 2 },
      { "a": 1 },
      { "a": 1, "b": 2, "c": 2 }
    ],
    { "a": 1, "c": 2 }
  )
]

let answers = [
  [{ first: "Tybalt", last: "Capulet" }],
  [{ "a": 1 }, { "a": 1 }, { "a": 1, "b": 2 }],
  [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }],
  [{ "a": 1, "b": 2, "c": 2 }]
]

for (i = 0; i < test.length; i++) {
    console.log (test[i] == answers[i], test[i], answers[i]);
}
