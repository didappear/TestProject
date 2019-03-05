// function func1(name) {
//     console.log("hello "+name);
//     return "hello!"
// }
// ret = func1('amy');
// console.log(ret);
//
//
// var func2 = new Function("name","console.log('hello '+name); return 'hello';");
// ret2 = func2('betty');
// console.log(ret2);
//
//
// function f(a,b){
//     alert(a+b);
// }
// var a=1;
// var b=2;
// console.log(f(a,b));


// function add(a,b,c,d){
//     console.log(a+b+c+d);
//     console.log(arguments.length);
//     console.log(arguments);
//     var result = 0;
//     for (var index in arguments){
//         // console.log("index is ",index)
//         result += arguments[index];
//         console.log("result is ",result);
//     }
// }
//
// add(1,22,33,4,5,6);

function func(a,b,c) {
    if (arguments.length != 3){
        throw new Error("function func needs 3 arguments," +
            "but "+arguments.length+"arguments are given!");
    } else {
        alert("sucess!");
    }
}
// func(1,2,3,4);

(function () {
    alert("hello amy")
})()

(function(arg) {
   console.log(arg);
})("a")







