![image-20220417184321058](img/image-20220417184321058.png)

转换数组，将多属性数组中的某个属性单拎出来成为新的数组

```js
let meeting_category = res.data.map((item)=>{
              return item.meeting_category;
```

过滤，提取数组中需要的数据

```js
let hyhy = meeting_category.filter((item)=>{
              return item === "行业会议"
            }).length;
```



js里异步需要时间响应，所以异步请求后的语句也可以在他前面执行

```js
axios.get(this.apiUrl)
        .then((res) => {          
        }).catch(err => console.error(err))
console.log(res); // 可能先执行


const res = await axios.get(this.apiUrl)
console.log(res); // 后执行 
```







案件关联、分类、地点信息、身份信息、趋势预测