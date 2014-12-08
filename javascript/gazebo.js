var user = prompt("One fateful day, as you're takaing a stroll through the woods, you happen upon a small clearing. In that clearing rests an old, large gazebo. What do you do? (FIGHT, LOOK, REASON, RUN)").toUpperCase();

switch(user) {
    case "FIGHT":
        var punch = prompt("Do you punch the gazebo? (YES/NO)").toUpperCase();
        var kick = prompt("Do you kick the gazebo? (YES/NO)").toUpperCase();
        if(punch === "YES" && kick === "YES") {
            console.log("You try to punch and kick the gazebo. You hurt your hand and foot, and also fall down, hurting your head.");
        } else if(punch === "YES") {
            console.log("You punch the gazebo. You break your hand.");
        } else if(kick === "YES") {
            console.log("You kick the gazebo. Your foot shatters.");
        } else {
            console.log("You slam your face into the gazebo. You're unconscious.");
        };
        break;
    case "LOOK":
        var leftEye = prompt("Do you look with your left eye?").toUpperCase();
        var rightEye = prompt("Do you look with your right eye?").toUpperCase();
        if(leftEye === "YES" || rightEye === "YES") {
            console.log("It looks like a gazebo. Hooray.");
        } else {
            console.log("Then, congratulations. You fail at the simple task of looking.");
        }
        break;
    case "REASON":
        console.log("You spout logical nonsense at the gazebo. It doesn't seem to care.");
        break;
    case "RUN":
        console.log("You run away from the gazebo. The gazebo stays put.");
        break;
    default:
        console.log("You " + user + ". The gazebo does nothing.");
}
