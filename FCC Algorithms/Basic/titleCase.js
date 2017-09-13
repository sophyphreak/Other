
function titleCase(str) {

  str = str.split(" ");

  for(i = 0; i < str.length; i++){
    str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1).toLowerCase();
  }

  return str.join(" ");
}

console.log(titleCase("i'm a little tea pot"));
