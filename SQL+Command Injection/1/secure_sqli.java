/**
 * Secure as snippet uses prepared statement (parameterised objects) where input is passed as parameters
 */
String query = "SELECT * FROM users WHERE usr = ? AND pwd = ?";
Connection conn = db.getConn();
PreparedStatement stmt = conn.preparedStatement(query);

stmt.setString(1, usr);
stmt.setString(2, pwd);

ResultSet rs = stmt.executeQuery(query);