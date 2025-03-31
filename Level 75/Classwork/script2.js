// Prompით მომხმარებელს შემოატანინეთ მისი სახელი, გვარი, ასაკი და ჰობი, შემდეგ ეს ინფორმაცია შეინახეთ ობიექტში, 
// ასევე ამ ობიექტს დაუმატეთ ფუნქცია, რომლის გამოძახებაზეც კონსოლში გამოიტანს "Welcome {name}"

const prompti = {
  name: prompt("Enter your name:"),
  surname: prompt("Enter your surname:"),
  age: prompt("Enter your age:"),
  hobby: prompt("Enter your hobby:"),

  welcome(){
    console.log("Welcome " + this.name)
  }


}


// შექმნილი ობიექტებიდან გამოიტანეთ მხოლოდ Keyები შემდეგ კი მხოლოდ Valueები

console.log(Object.keys(prompti))
console.log(Object.values(prompti))

// შექმნილ ობიექტს გადაუარეთ for ციკლით და გამოიტანეთ key და value შემდეგი ფორმატით: "{key} is {value}"

for (let i in prompti) {
  console.log(i + " is " + prompti[i])
}