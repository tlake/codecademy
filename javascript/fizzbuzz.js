// commented code is original method; valid, but not exactly how
// codecademy wanted it formatted.

var numberGen = function(upper) {
    var list = [];
    for(var i = 1; i < upper + 1; i++) {
        list.push(i);
    }
    return list;
};


var fizzBuzz = function(sourceList) {
    var tempList = [];
    for(var i = 0; i < sourceList.length; i++) {
        if(sourceList[i] % 3 === 0 && sourceList[i] % 5 === 0) {
            // tempList.push("FizzBuzz");
            console.log("FizzBuzz");
        } else if(sourceList[i] % 3 === 0) {
            // tempList.push("Fizz");
            console.log("Fizz");
        } else if(sourceList[i] % 5 === 0) {
            // tempList.push("Buzz");
            console.log("Buzz");
        } else {
            // tempList.push(sourceList[i]);
            console.log(sourceList[i]);
        }
    };
    // return tempList;
};


var numbers = numberGen(20);
// console.log(numbers);
// var newNumbers = fizzBuzz(numbers);
// console.log(newNumbers);
fizzBuzz(numbers);
