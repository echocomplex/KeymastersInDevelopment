import java.sql.Connection;
import java.sql.Statement;
import java.sql.SQLException;
import java.sql.DriverManager;

public class Main {
    public static void main (String args[]) {
        try {
            Connection connection = DriverManager.getConnection("jdbc:sqlite:TelegramBotUsers.db");
            Statement statement = connection.createStatement();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
