
function spinalCase(str) {
  let reCapitalWithoutSpace = new RegExp(/[a-z][A-Z]/, 'g');
  let reCapital = new RegExp(/[A-Z]/, 'g');
  let reSpace = new RegExp(/ /, 'g');
  let reUnderscore = new RegExp(/_/, 'g');

  str = str.replace(reSpace, () => "-");
  str = str.replace(reUnderscore, () => "-");
  str = str.replace(reCapitalWithoutSpace, (subStr) => {
    return subStr[0] + "-" + subStr[1].toLowerCase();
  });
  str = str.replace(reCapital, (char) => char.toLowerCase());



  return str;
}
console.log(
  '\n', spinalCase("This Is Spinal Tap"), "\n",
  spinalCase("thisIsSpinalTap"), '\n',
  spinalCase("The_Andy_Griffith_Show"), '\n',
  spinalCase("Teletubbies say Eh-oh"), '\n',
  spinalCase("AllThe-small Things")
);
