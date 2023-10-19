/**
 * Vulnerable as code sends username and password via HTTP and not HTTPS
 * Also uses GET instead of POST for secure data (storing credentials in web logs)
 */

String url = "http://my-service.cloud.biz/Login?usr="+usr+"&pwd="+pwd;
URL obj = new URL(url);
HTTPURLConnection con = (HTTPURLConnection) obj.openConnection();

con.setRequestMethod("GET");
con.setRequestProperty("User-Agent", USER_AGENT);