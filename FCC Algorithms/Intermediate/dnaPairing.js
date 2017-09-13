
function pairElement(str) {

  let answer = [];

  for (index in str) {
    switch(str[index]) {
      case "A":
        answer.push(["A", "T"]);
        break;
      case "T":
        answer.push(["T","A"]);
        break;
      case "C":
        answer.push(["C", "G"]);
        break;
      case "G":
        answer.push(["G", "C"]);
        break;
    }
  }

  return answer;
}

pairElement("GCG");
