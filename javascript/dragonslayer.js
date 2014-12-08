var slaying = true;

var youHit = function() {
    if(Math.random() > 1 / 4) {
        return true;
    } else {
        return false;
    }
}

var totalDamage = 0;


while(slaying) {
    
    if(youHit()) {
        var damageThisRound = Math.floor(Math.random() * 5 + 1);
        console.log("You've struck the dragon! Hit for " 
            + damageThisRound + ".");

        totalDamage += damageThisRound;
        
            if(totalDamage >= 8) {
                
                console.log("Yeah! You fucked that dragon up good!");
                slaying = false;
            }
            
    } else {
        console.log("You fucked up! You've died from being on fire.");
        slaying = false;
    }
    
}
