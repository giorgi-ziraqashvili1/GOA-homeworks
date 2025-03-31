// 2)for-ციკლის გამოყენებით იპოვეთ სიაში ყველაზე დიდი და ყველაზე პატარა რიცხვები

var numbers = [3, 7, 2, 9, 5, 1, 8];
var min = numbers[0]
var max = numbers[0]

for (var num of numbers) {
    if (num < min) min = num;
    if (num > max) max = num;
}

console.log(min)
console.log(max)