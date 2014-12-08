var friends = {};

friends.bill = {
    firstName: "Bill",
    lastName: "Grates",
    number: "98",
    address: ['Open Windows', 'Microsoft', 'WI', '95,98,7,8']
};

friends.steve = {
    firstName: "Steve",
    lastName: "Knobs",
    number: "80085",
    address: ["Branch #3", "Apple Tree", "MA", "1375"]
};

friends.cat = {
    firstName: "Kitty",
    lastName: "Cat",
    number: "287619702489090",
    address: ["Patch of Sunlight", "Living Room", "APT", "45569"]
};

console.log(friends);

var list = function(contacts) {
    for(var each in contacts) {
        console.log(each);
    }
}

var search = function(name) {
    for(var each in friends) {
        if(name.toLowerCase() === friends[each].firstName.toLowerCase()) {
            console.log("First Name: " + friends[each].firstName);
            console.log("Last Name: " + friends[each].lastName);
            console.log("Number: " + friends[each].number);
            console.log("Address: " + friends[each].address[0]);
            console.log("         " + friends[each].address[1] + " " + friends[each].address[2] + " " + friends[each].address[3]);
            return friends[each];
        }
    }
}

list(friends);
search("kitty");
