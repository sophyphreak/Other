


function myReplace(str, before, after) {

  if (before[0] != before[0].toUpperCase()) {
    str = str.replace(before, after);
  } else {
    after = after.replace(/\b\w/g, l => l.toUpperCase());
    str = str.replace(before, after);
  }
  return str;
}

myReplace("A quick brown fox jumped over the lazy dog", "jumped", "leaped");
