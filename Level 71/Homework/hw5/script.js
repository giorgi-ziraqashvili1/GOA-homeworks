// 
// 5)Splice მეთოდის გამოყენებით ჩაანაცვლეთ სიაში ყველა უარყოფითი რიცხვი 0 - ით


var numbers = [4, -2, 7, -5, 10, -8, 3];

for (var i = 0; i < numbers.length; i++) {
    if (numbers[i] < 0) {
        numbers.splice(i, 1, 0); 
    }
}

console.log(numbers);