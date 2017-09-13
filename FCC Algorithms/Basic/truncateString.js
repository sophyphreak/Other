
function truncateString(str, num) {
  if(str.length <= num) {
    return str;
  }
  if(num <= 3) {
    str = str.slice(0, num);
    str += "...";
    return str;
  }
  str = str.slice(0, num - 3);
  str += "...";
  return str;
}

console.log(truncateString("A-", 1));
