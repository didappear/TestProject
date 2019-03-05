// alert("hello");
// info = "确认提交吗？";
// re1 = confirm(info);
// console.log(re1);
// re = prompt("请输入密码：","123");
// console.log(re);

// open("https://www.baidu.com");
// open("https://www.jianshu.com","新的窗口名字",
//     "width=200,resizable=no,height=300");
//


var num = Math.round(Math.random()*100);
function acceptInput() {
    var usernum = prompt("请输入一个0~100之间的数字：","0");
    if (isNaN(+usernum)){
        alert("请输入有效数字！");
        acceptInput();
    }else if(usernum == null){
        close();
    }else if (usernum < num){
        alert("您输入的小了！");
        acceptInput();
    } else if (usernum > num){
        alert("您输入的大了！");
        acceptInput();
    }else {
        var result = confirm("恭喜你！答对了！，是否继续游戏？");
        if(result){
            num = Math.round(Math.random()*100);
            acceptInput();
        }else {
            close();
        }
    }
}

// acceptInput();


function showtime() {
    var now = new Date().toLocaleString();
    var ele = document.getElementById("input_datetime");
    // html标签就是一个对象，获取属性用点语法.
    ele.value = now.toString();
}

var ID;
function begin() {
    if (ID == undefined){
        showtime();
        ID = setInterval(showtime,1000);
    }
}

function end() {
    clearInterval(ID);
    ID = undefined;
}

function func(){
    console.log("hello!")
}
intervalID = setInterval(func, 1000);
clearInterval(intervalID);

timeoutID = setTimeout(func,1000);
clearTimeout(timeoutID);




















