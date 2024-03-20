/*

Database for Keymaster's Telegram Bot
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

*/

package Database.DatabaseClassesJava;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;

public class TelegramBotDatabase {
    private Connection connection;
    private Statement statement;
    private int chatID;

    public TelegramBotDatabase (int chatID) {
        try {
            try {
                Class.forName("org.sqlite.JDBC");
            }
            catch (ClassNotFoundException e) {
                // Обработка исключения: вывод сообщения или логирование ошибки
                e.printStackTrace();
            }
            this.connection = DriverManager.getConnection("jdbc:sqlite:/Users/mac/Documents/project-codes/multi-languages/KeymastersInDevelopment/Database/DatabaseFiles/TelegramBotUsers.db");
            this.statement = this.connection.createStatement();
            this.chatID = chatID;
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addUser () {
        String query =
                """
                INSERT OR IGNORE INTO users (chat_id, language, login_status) 
                VALUES (?, ?, ?)
                """;
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, this.chatID);
            statement.setString(2, "RU");
            statement.setBoolean(3, false);
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
                WHERE chat_id = ?
                """;
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setString(1, language);
            statement.setInt(2, this.chatID);
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
                WHERE chat_id = ?
                """;
        String language;
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, this.chatID);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                language = resultSet.getString("language");
            }
            else {
                language = "RU";
            }
        } catch (SQLException e) {
            language = "RU";
            e.printStackTrace();
        }
        return language;
    }

    public void setLoginStatus (boolean status) {
        String query =
                """
                UPDATE users
                SET login_status = ?
                WHERE chat_id = ?
                """;
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setBoolean(1, status);
            statement.setInt(2, this.chatID);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public boolean getLoginStatus () {
        String query =
                """
                SELECT login_status
                FROM users
                WHERE chat_id = ?
                """;
        boolean loginStatus;
        try (PreparedStatement statement = connection.prepareStatement(query)) {
            statement.setInt(1, this.chatID);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                loginStatus = resultSet.getBoolean("login_status");
            }
            else {
                loginStatus = false;
            }
        }
        catch (SQLException e) {
            loginStatus = false;
            e.printStackTrace();
        }
        return loginStatus;
    }

    public void closeConnection () {
        try {
            if (this.statement != null) {
                this.statement.close();
            }
            if (this.connection != null) {
                this.connection.close();
            }
        }
        catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
