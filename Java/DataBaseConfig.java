public class DatabaseConfig {
    private String host;
    private int port;
    private String username;
    private String password;

    public DatabaseConfig(String host, int port, String username, String password) {
        if (host == null) {
            this.host = "localhost";
        }
        if (port == 0) {
            this.port = 5432;
        }
        if (username == null) {
            this.username = username;
        }
        if (password == null) {
            this.password = "password";
        }
    }
    public String get_host(){
        return host;
    }
    public int get_port(){
        return port;
    }
    public String get_password(){
        return password;
    }
    public String get_username(){
        return username;
    }
 
}