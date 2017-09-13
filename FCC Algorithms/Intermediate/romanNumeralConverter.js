
function convertToRoman(num) {

  var res = [];

  while (num > 0) {
    console.log(num);
    if (num >= 1000) {
      res.push("M");
      num -= 1000;
    } else if (num >= 900) {
      res.push("CM");
      num -= 900;
    } else if (num >= 500) {
      res.push("D");
      num -= 500;
    } else if (num >= 400) {
      res.push("CD");
      num -= 400;
    } else if (num >= 100) {
      res.push("C");
      num -= 100;
    } else if (num >= 90) {
      res.push("XC");
      num -= 90;
    } else if (num >=50) {
      res.push("L");
      num -= 50;
    } else if (num > 40) {
      res.push("XL");
      num -= 40;
    } else if (num >= 10) {
      res.push("X");
      num -= 10;
    } else if (num >= 9) {
      res.push("IX");
      num -= 9;
    } else if (num >= 5) {
      res.push("V");
      num -= 5;
    } else if (num >= 4) {
      res.push("IV");
      num -= 4;
    } else if (num >= 1) {
      res.push("I");
      num -= 1;
    }
  }
  return res.join("");
}

console.log(convertToRoman(36));
