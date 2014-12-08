/*jshint multistr:true */

var text = "hodor hodor hodor hodor hodor Tanner hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor Tanner hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor hodor hodor hodor Tanner Tanner hodor hodor \
hodor hodor hodor Tanner hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
Tanner hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor hodor \
hodor hodor hodor hodor Tanner hodor hodor hodor hodor hodor hodor";

var myName = "Tanner";

var re = new RegExp(myName, "g");

var hits = text.match(re);

if(hits[0] === null){
    console.log("Your name wasn't found!");
}
else {
    console.log(hits);
    console.log("Number of hits: " + hits.length);
}
