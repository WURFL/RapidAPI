const axios = require("axios");
let payload = {
    "lookup_headers": {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; ASUS_Z017D Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
        "content-Type": "application/json",
        "x-requested-with":"XMLHttpRequest"
    },
    // Uncomment the next lines to enable a filter for the given capabilities
    //"requested_caps": ["is_tablet"],
    //"requested_vcaps": ["complete_device_name", "form_factor"]
}

let rapidapiKey = process.env.RAPIDAPI_KEY
let rapidapiHost = process.env.RAPIDAPI_HOST
let url = `https://${rapidapiHost}/v2/lookuprequest/json`

if (rapidapiKey == null || rapidapiKey === "" || rapidapiHost == null || rapidapiHost === ""){
    console.log("You must set RAPIDAPI_KEY and RAPIDAPI_HOST environment variables to use this code example")
}

axios({
    "method":"POST",
    "url":url,
    "headers":{
        "content-type":"application/json",
        "x-rapidapi-key": rapidapiKey,
        "x-rapidapi-host": rapidapiHost,
        "useQueryString":true
    },"data": payload
})
    .then((response)=>{
        console.log(response.data)
    })
    .catch((error)=>{
        console.log(error)
    })