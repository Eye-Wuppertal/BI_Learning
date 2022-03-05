const express = require("express");
//引入封装好的mysql文件
const db = require("./test");

const server =express();


// get请求，要拿到前端传过来的数据，使用query
// post请求，传到前端去的数据，使用body
server.get("/getCatName",async(request,response,next)=>{
    let cnt = request.query.cnt;
    let params = [cnt];
    let sql = "SELECT * FROM app_cat_cnt WHERE cnt = ?;";
    let result = await db.exec(sql,params);

    response.json(result);
})

server.listen(8080,()=>{
    console.log("服务器启动完毕！");
})