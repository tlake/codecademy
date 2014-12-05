// Wrapping the whole game into a function
var playGame = function() {


    // Function to make sure the user's choice is valid
    var checkInput = function(choice) {
        var acceptableChoices = ["rock", "paper", "scissors"];
        for(var i in acceptableChoices) {
            if(choice === acceptableChoices[i]) {
                return true;
            }
        }
        return false;
    };


    // Function to get the user's choice
    var getUserChoice = function() {
        var choice;
        while(!checkInput(choice)) {
            choice = prompt("Do you choose rock, paper or scissors?").toLowerCase();
        }
        return choice;
    };


    // Function to get the computer's choice
    var getComputerChoice = function() {
        var choice = Math.random();

        if(computerChoice < 1 / 3) {
            return "rock";
        }
        else if(computerChoice <= 2 / 3) {
            return "paper";
        }
        else {
            return "scissors";
        }
    };


    // Function to perform game logic
    var compare = function(choice1, choice2) {
        if(choice1 === choice2) {
            return 0;
        }
        else if(choice1 === "rock") {
            if(choice2 === "scissors") {
                return "rock wins";
            }
            else {
                return "paper wins";
            }
        }
        else if(choice1 === "paper") {
           if(choice2 === "rock") {
                return "paper wins";
            }
            else {
                return "scissors wins";
            }
        }
        else {
            if(choice2 === "rock") {
                return "rock wins";
            }
            else {
                return "scissors wins";
            }
        }
    };


    // Game progression
    
    var userChoice = getUserChoice();
    
    var computerChoice = getComputerChoice();
    
    console.log("Player chooses " + userChoice);
    console.log("Computer chooses " + computerChoice);
    
    var result = compare(userChoice, computerChoice);
    
    if(result === 0) {
        console.log("Tie game - try again!");
        playGame();
    }
    else {
        console.log(result);
    }

};

playGame();
