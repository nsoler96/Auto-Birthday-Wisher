#include <iostream>
#include <mysql_driver.h>
#include <mysql_connection.h>
#include <cppconn/prepared_statement.h>
#include <cppconn/resultset.h>

using namespace std;

int main() {
    // MySQL server connection details
    string server = "tcp://127.0.0.1:3306";  // MySQL server address
    string username = "root";                 // MySQL username
    string password = "Soleryo52!!";                     // MySQL password (leave empty if no password)
    string database = "todo_list";            // Database name

    try {
        // Create a connection to the MySQL server
        sql::mysql::MySQL_Driver *driver;
        sql::Connection *con;
        driver = sql::mysql::get_mysql_driver_instance();
        con = driver->connect(server, username, password);
        
        // Connect to the specific database
        con->setSchema(database);

        // Query the tasks table
        sql::Statement *stmt = con->createStatement();
        sql::ResultSet *res = stmt->executeQuery("SELECT * FROM tasks");

        // Print out the tasks
        cout << "Your To-Do List:" << endl;
        while (res->next()) {
            cout << "ID: " << res->getInt("id")
                 << " | Description: " << res->getString("description")
                 << " | Status: " << res->getString("status") << endl;
        }

        // Clean up
        delete res;
        delete stmt;
        delete con;
    } catch (sql::SQLException &e) {
        cerr << "# ERR: " << e.what() << endl;
    }

    return 0;
}
