/*

Passwords Database for Keymaster's Project
This code was written by echo complex (https://t.me/echoscomplex)
License - GNU GPLv2 Keymaster's © 2024 (CEO - echo complex (https://t.me/echoscomplex))
All rights reserved.

P.S. Command to create Database: CREATE TABLE AnyUsernameKalMamba4Exaple (service_name TEXT, password TEXT NOT NULL)

*/


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.PreparedStatement;
import java.util.ArrayList;
import java.util.List;


public class PasswordDatabase {
    private Connection connection;
    private String username;

    public PasswordDatabase (String username, String databasePath) {
        try {
            this.connection = DriverManager.getConnection("jdbc:sqlite:" + databasePath);
            this.username = username;
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void addUser () {
        String query = String.format(
                """
                CREATE TABLE IF NOT EXISTS "%s" (service_name TEXT NOT NULL, password TEXT NOT NULL)
                """, this.username
        );
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addPassword (String serviceName, String servicePassword) {
        String query = String.format(
                """
                INSERT INTO %s (service_name, password)
                VALUES (?, ?)
                """, this.username
        );
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, serviceName);
            statement.setString(2, servicePassword);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<String[]> getAll () {
        List<String[]> allRows = new ArrayList<>();
        String query = String.format(
                """
                SELECT * FROM %s
                """, this.username
        );
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            ResultSet result = statement.executeQuery();
            ResultSetMetaData resultMetaData = result.getMetaData();
            int columnCount = resultMetaData.getColumnCount();
            while (result.next()) {
                String[] row = new String[2];
                row[0] = result.getString("service_name");
                row[1] = result.getString("password");
                allRows.add(row);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return allRows;
    }

    public void deletePassword (String serviceName, String password) {
        String query = String.format(
                """
                DELETE FROM %s
                WHERE service_name = ? AND password = ?
                """, this.username
        );
        try (PreparedStatement statement = this.connection.prepareStatement(query)) {
            statement.setString(1, serviceName);
            statement.setString(2, password);
            statement.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        }
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