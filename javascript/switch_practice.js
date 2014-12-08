// Write your code below!
var theRoom = function() {

    var direction = prompt("You stand in a nondescript room. There are exits to the north, south, east, and west. Where do you go?").toLowerCase();
    
    switch(direction) {
        case 'north':
            console.log("You go north. You freeze to death.");
            break;
        case 'south':
            console.log("You go south. You're horribly murdered by everyone in King's Landing.");
            break;
        case 'east':
            console.log("You're murdered to settle an unreasonably large debt accrued in the house of the rising sun.");
            break;
        case 'west':
            console.log("You're vaporized as the sun quite literally sets on you.");
            break;
        case 'dennis':
            console.log("Congrats! You've found the way out! You die of old age (by which I mean elderly folks, of course.)");
            break;
        default:
            console.log("You fail to leave the room. I don't see how, because there are four open doors. You die of stupidity and dehydration. Good job.");
    }
    
};

theRoom();
