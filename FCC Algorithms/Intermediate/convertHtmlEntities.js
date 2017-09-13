
function convertHTML(str) {

  let targetChar = ["&", "<", ">", '"', "'"];
  let targetObj = {
                  "&": "&amp;",
                  "<": "&lt;",
                  ">": "&gt;",
                  '"': "&quot;",
                  "'": "&apos;"
                 };
  let find;
  let re;

  for(let index in targetChar) {
    find = targetChar[index];
    re = new RegExp(find, 'g');
    str = str.replace(re, targetObj[targetChar[index]]);
  }

  return str;
}
console.log(
  convertHTML("Hamburgers < Pizza < Tacos"), "\n",
  convertHTML('Stuff in "quotation marks"')
);
