package rapidapi;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

import static java.lang.System.*;

public class WurflRapidApiExample {

    /**
     * This code sample uses Java 15 (text blocks, finally!) to illustrate a minimal WURFL RapidAPI call.
     * If you want to select specific capabilities, you have to add fields "requested_caps": and/or "requested_vcaps"
     * for example
     * {
     *    "lookup_headers": {
     *        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; ASUS_Z017D Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/539.36"
     *    },
     *    "requested_caps":["brand_name", "model_name"]
     *    "requested_vcaps":["form_factor"]
     * }
     */
    public static void main(String args[]){

        var rapidApiKey = getenv("RAPIDAPI_KEY");
        var rapidApiHost = getenv("RAPIDAPI_HOST");
        var payload = """
                {
                	"lookup_headers": {
                		"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; ASUS_Z017D Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/539.36"
                	}
                }
                """;

        if(rapidApiKey == null || rapidApiKey.isBlank() || rapidApiHost == null || rapidApiHost.isBlank()){
            out.println("You must set RAPIDAPI_KEY and RAPIDAPI_HOST to use this code example");
            exit(1);
        }
        var url = "https://" + rapidApiHost +"/v2/lookuprequest/json";
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("x-rapidapi-host", rapidApiHost)
                .header("x-rapidapi-key", rapidApiKey)
                .header("content-type", "application/json")
                .method("POST", HttpRequest.BodyPublishers.ofString(payload))
                .build();
        HttpResponse<String> response = null;
        try {
            response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        }
        catch (Exception e){
            out.println("Error: " + e.getMessage());
            out.println("Terminating sample app");
            exit(1);
        }
        out.println(response.body());
    }
}
