package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {

	rapidApiKey := os.Getenv("RAPIDAPI_KEY")
	rapidApiHost := os.Getenv("RAPIDAPI_HOST")

	if rapidApiKey == "" || rapidApiHost == "" {
		fmt.Println("You must specify RAPIDAPI_KEY and RAPIDAPI_HOST to run this code example")
		os.Exit(1)
	}

	url := "https://" + rapidApiHost + "/v2/lookuprequest/json"

	payload := strings.NewReader("{\t\"lookup_headers\": {\t\t\"User-Agent\": \"Mozilla/5.0 (Linux; Android 6.0; ASUS_Z017D Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/539.36\",                \"content-Type\": \"application/json\",                \"x-requested-with\":\"XMLHttpRequest\"\t}}")
	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("x-rapidapi-host", rapidApiHost)
	req.Header.Add("x-rapidapi-key", rapidApiKey)
	req.Header.Add("content-type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)

	fmt.Println(string(body))

}
