var getReview = function (movie) {
    switch(movie.toLowerCase().replace(/\s+/g, '')) {
        case "toystory2":
            return "Great story. Mean prospector.";
        case "findingnemo":
            return "Cool animation, and funny turtles.";
        case "thelionking":
            return "Great songs.";
        default:
            return "I don't know!";
    }
};
