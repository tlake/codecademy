var reviewsLibrary = {};

reviewsLibrary.toyStory2 = {
    Title: "Toy Story 2",
    Review: "Great story. Mean prospector."
};
    
reviewsLibrary.findingNemo = {
    Title: "Finding Nemo",
    Review: "Cool animation, and funny turtles."
};
    
reviewsLibrary.theLionKing = {
    Title: "The Lion King",
    Review: "Great songs."
};


var getReview = function (movie) {
    var formattedMovie = movie.replace(/\s+/g, '');
    formattedMovie = formattedMovie.toLowerCase();
    switch(true) {
        case (formattedMovie === "toystory2"):
            return reviewsLibrary.toyStory2.Review
        case (formattedMovie === "findingnemo"):
            return reviewsLibrary.findingNemo.Review
        case (formattedMovie === "thelionking"):
            return reviewsLibrary.theLionKing.Review
        default:
            return "I don't know!";
    }
    
};

getReview("The lion KiNG");
