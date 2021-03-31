const axios = require("axios");

let rapidapiKey = process.env.RAPIDAPI_KEY
let rapidapiHost = process.env.RAPIDAPI_HOST
let url = `https://${rapidapiHost}/v2/lookupdeviceid/json`

if (rapidapiKey == null || rapidapiKey === "" || rapidapiHost == null || rapidapiHost === ""){
    console.log("You must set RAPIDAPI_KEY and RAPIDAPI_HOST environment variables to use this code example")
}

axios({
    "method":"POST",
    "url":url,
    "headers":{
        "content-type":"application/json",
        "x-rapidapi-host": rapidapiHost,
        "x-rapidapi-key": rapidapiKey,
        "useQueryString":true
    },"data":{
        "wurfl_id":"asus_z017d_ver1"
    }
})
    .then((response)=>{
        console.log(response.data)
    })
    .catch((error)=>{
        console.log(error)
    })