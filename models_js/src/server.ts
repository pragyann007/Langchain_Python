import express from "express"
const app = express();

let port = process.env.PORT || 8080 ;

app.get("/",(req,res)=>{
    res.send("Hi i am Pragyan")
})




app.listen(port,()=>{
    console.log(`server is running on port ${port}`)
})