/*

Users Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

P.S. Command to create Database: CREATE TABLE users (username TEXT PRIMARY KEY, language VARCHAR(2) NOT NULL, chat_id INTEGER,  password TEXT NOT NULL)

*/


import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;


public class UsersDatabase {
    private Connection connection;
    private String username;

    public UsersDatabase (String username, String databasePath) {
        try {
            this.connection = DriverManager.getConnection("jdbc:sqlite:"+databasePath);
            this.username = username;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static String hashPassword (String password) {
        String hashedPassword;
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(password.getBytes(StandardCharsets.UTF_8));
            BigInteger i = new BigInteger(1, hash);
            hashedPassword = i.toString(16);
        } catch (Exception e) {
            e.printStackTrace();
            hashedPassword = "";
        }
        return hashedPassword;
    }

    public static String findUsernameByChatID (int chatID, String databasePath) {
        String username;
        try {
            Connection connection = DriverManager.getConnection("jdbc:sqlite:"+databasePath);
            String query =
                     """
                     SELECT username
                     FROM users
                     WHERE chat_id = ?
                     """;
            try (PreparedStatement statement = connection.prepareStatement(query)) {
                statement.setInt(1, chatID);
                ResultSet result = statement.executeQuery();
                if (result.next()) {
                    username = result.getString("username");
                }
                else {
                    username = "";
                }
            } catch (SQLException e) {
                e.printStackTrace();
                username = "";
            }
        } catch (Exception e) {
            e.printStackTrace();
            username = "";
        }
        return username;
    }

    public void addUser (String language, String password) {
        String hashedPassword = hashPassword(password);
        String query =
            """
            INSERT OR IGNORE INTO users (username, language, password) 
            VALUES (?, ?, ?)
            """;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, this.username);
            statement.setString(2, language);
            statement.setString(3, hashedPassword);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void setLanguage (String language) {
        String query =
                """
                UPDATE users
                SET language = ?
                WHERE username = ?
                """;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, language);
            statement.setString(2, this.username);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public String getLanguage () {
        String query =
                """
                SELECT language
                FROM users
                WHERE username = ?
                """;
        String language;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, this.username);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                language = result.getString("language");
            }
            else {
                language = "RU";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            language = "RU";
        }
        return language;
    }

    public void setPassword (String password) {
        String hashedPassword = hashPassword(password);
        String query =
                """
                UPDATE users
                SET password = ?
                WHERE username = ?
                """;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, hashedPassword);
            statement.setString(2, this.username);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Boolean authenticate (String password) {
        String query =
                """
                SELECT password
                FROM users
                WHERE username = ?
                """;
        String databaseHash;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, this.username);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                databaseHash = result.getString("password");
            }
            else {
                databaseHash = "";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            databaseHash = "";
        }

        String hashedPassword = hashPassword(password);
        return hashedPassword.equals(databaseHash);
    }

    public void setChatID (int chatID) {
        String query =
                """
                UPDATE users
                SET chat_id = ?
                WHERE username = ?
                """;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setInt(1, chatID);
            statement.setString(2, this.username);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public int getChatID () {
        String query =
                """
                        SELECT chat_id
                        FROM users
                        WHERE username = ?
                        """;
        int chatID;
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, this.username);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                chatID = result.getInt("chat_id");
            } else {
                chatID = 0;
            }
        } catch (SQLException e) {
            e.printStackTrace();
            chatID = 0;
        }
        return chatID;
    }

    public void closeConnection () {
        try {
            if (this.connection != null) {
                this.connection.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}