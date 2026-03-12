package database;

public class DatabaseConfig {
    private final String host;
    private final int port;
    private final String username;
    private final String password;

    static void main(String[] args) {
        DatabaseConfig dc = new DatabaseConfig();
        System.out.println(dc);

        DatabaseConfig new_user = new DatabaseConfig("Nkuli",619,"nksthjhb025","popofarm");
        System.out.println(new_user);

    }
    public DatabaseConfig(String host, int port, String username, String password) {
        this.host = host;
        this.port = port;
        this.username = username;
        this.password = password;
    }


    public DatabaseConfig(String host, int port) {
        this(host, port, "admin", "password");
    }

    // Overloaded Cosntructor with zero arguments
    public DatabaseConfig() {
        this("localhost",5347
                ,"admin","password");
    }

    /// Accesor methods
    public String getHost(){return host;}
    public int getPort(){return port;}
    public String getPassword(){
        String mask = "";
        for (int i = 0; i < password.length();i ++){
            mask += "*";
        }
        return mask;
    }
    public String getUsername(){return username;}

    @Override
    public String toString(){
        return "Host: " + getHost() + '\n'
                + "Port:  " + getPort() + '\n'
                + "Password:   " + getPassword() + '\n'
                + "Username: " + getUsername() + '\n';
    }
}