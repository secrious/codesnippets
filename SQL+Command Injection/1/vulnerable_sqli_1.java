/**
 * Vulnerable as input is concatenated to OS command
 */
String updateServer = request.getParameter("updateServer");
String cmdProcessor = Utils.isWindows() ? "cmd" : "/bin/sh";
String command = cmdProcessor + "-c ping " + updateServer;
Process p = Runtime.getRuntime().exec(command);