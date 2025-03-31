// 3)შექმენით სია, ამ სიაში შეინახეთ String-ტიპის მონაცემები და for-ციკლის გამოყენებით ახალ სიაში დაამატეთ ძველი სიიდან ყოველი სიტყვის პირველი ასო


var  list = ["gio", "gabrieli", "vano", "mariami"]

var new_word = []

for (var i = 0; i < list.length; i++ ) {
    new_word[i] = list[i][0];
    
}

console.log(new_word)