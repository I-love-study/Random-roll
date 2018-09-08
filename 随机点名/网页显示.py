from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    fp=open(r"名单.txt")
    name=[]
    for lines in fp.readlines():
        lines=lines.replace("\n","")
        name.append(lines)
    fp.close()
    info = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>点名器（Make by I_Love_Study from Class 7)</title>
<style>
#Uname{
width: 300px;
height: 200px;
border:3px solid green;
margin:0 auto;
margin-top: 100px;
font-size:50px;
font-weight: 800;
text-align: center;
line-height: 200px; 
}
.btn{
width: 60px;
height: 200px;
margin:0 auto;
margin-top:20px;
}
.btn button{
width: 50px;
}
</style>
</head>
<body>
<div id="Uname">我爱学习</div>
<div class="btn">
<button onclick="demo()" id="bt">开始</button>
<!-- <button onclick="stop()">结束</button> -->
</div>
<script>
//拓展 将选过的名字 从数组中剔除
var Uname=document.getElementById('Uname');
var arr=%s
var btn=document.getElementById('bt');
var clock=0;
// 如果为真开始执行 如果为假的停止
var st=true;


function demo(){
if(st){
start();
btn.innerHTML="结束";
st=false;


}else{
stop();
btn.innerHTML="开始";
st=true;


}
}


// 开始函数
function start(){
clock=setInterval(function(){
var inde=rand(0,arr.length-1);
console.log(inde);
Uname.innerHTML=arr[inde];
},50)
}


// 结束点名
function stop(){
clearInterval(clock);
}




// 封装获取随机数 函数
function rand(m,n){
return Math.floor(Math.random()*(n-m+1)+m);
}
</script>
</body>
</html>
""" % (name)
    return info

if  __name__=="__main__":
    app.run()
    #(host='192.168.0.105',port=9000)
