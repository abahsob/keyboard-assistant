const keyboard = 'tiuwyqerpokdfjs;glha.c,mvnbz?x';

const qwerty = 'qwertyuiopasdfghjkl;zxcvbnm,./';
cursor="|"
document.addEventListener(
  'keydown',
  (event) => {
    var name = event.key;
    // Alert the key name and key code on keydown
    let idx = qwerty.indexOf(name);
    const input = document.getElementById('inp');
    console.log(name, idx);
    if (name == 'Backspace') {
      backspace();
      document.getElementById('Backspace').classList.add('bg-gray-300');
    }
    if (name == ' ') {
      space();
      document.getElementById('Space').classList.add('bg-gray-300');
    }
    if (idx != -1) {
      value += keyboard[idx];
      input.value = value+cursor;
      document.getElementById(`${keyboard[idx]}`).classList.add('bg-gray-300');
    }
  },
  false
);
document.addEventListener('keyup', (event) => {
  var name = event.key;
  let idx = qwerty.indexOf(name);
  if (name == 'Backspace')
    document.getElementById('Backspace').classList.remove('bg-gray-300');

  if (name == ' ')
    document.getElementById('Space').classList.remove('bg-gray-300');

  if (idx != -1) {
    document.getElementById(`${keyboard[idx]}`).classList.remove('bg-gray-300');
  }
});

let value = '';

function add_char(id) {
  const input = document.getElementById('inp');
  value += id;
  input.value = value+cursor;
}

function backspace() {
  const input = document.getElementById('inp');
  value = value.slice(0, value.length - 1);
  input.value = value+cursor;
}

function space() {
  const input = document.getElementById('inp');
  value += ' ';
  input.value = value+cursor;
}

var text = `<div class="flex">`;
for (let i = 0; i < 10; i++) {
  text =
    text +
    `<button id="${keyboard[i]}" class="rounded-lg w-14 h-14 border-2 border-gray-700 mx-1 my-[4px] active:bg-gray-400 hover:bg-gray-300" onclick="add_char(this.id)">${keyboard[i]}</button>`;
}
text += `</div><div class="flex ml-5">`;
for (let i = 10; i < 20; i++) {
  text =
    text +
    `<button id="${keyboard[i]}" class="rounded-lg w-14 h-14 border-2 border-gray-700 mx-1 my-[4px] active:bg-gray-400 hover:bg-gray-300" onclick="add_char(this.id)">${keyboard[i]}</button>`;
}
text += `</div><div class="flex ml-10">`;
for (let i = 20; i < 30; i++) {
  text =
    text +
    `<button id="${keyboard[i]}" class="rounded-lg w-14 h-14 border-2 border-gray-700 mx-1 my-[4px] active:bg-gray-400 hover:bg-gray-300" onclick="add_char(this.id)">${keyboard[i]}</button>`;
}
text += '</div>';

document.getElementById('keyb').innerHTML = text;
