## PyServer - The Python HTTP Server

PyServer is a lightweight Python HTTP server that allows you to quickly set up a local web server for testing and development purposes. It provides a simple and easy-to-use interface for serving files and handling HTTP requests.

### Technical Details:

The PyServer script is written in Python and utilizes the built-in http.server module for handling HTTP requests. It supports both IPv4 and IPv6 addresses and listens on port 80 by default. The server runs on the 0.0.0.0 IP address, making it accessible from any network interface.

The script includes a command-line option to set up OpenSSL, which is useful for enabling secure HTTPS connections. When running the script with the -setup ssl flag, PyServer installs OpenSSL and adds it to the system's PATH environment variable. This feature is currently supported on Windows and Linux platforms.

PyServer logs its activities using the logging module, providing informative messages about the server's status, IP, and port details. It also notifies users about certain commands that may cause temporary system delays.

## Output Examples:

1. Starting the PyServer without SSL setup:
```batch
Welcome to PyServer - The Python HTTP Server!
Server Details:
IP: 0.0.0.0
Port: 80
To terminate the connection, please enter 'EXIT'.
Please be aware that certain commands may result in temporary system delays.

Server started. Press 'CTRL+C' to terminate.
```

2. Starting the PyServer with SSL setup:
```batch
Installing OpenSSL...
OpenSSL installation completed.
Adding OpenSSL to system PATH...
OpenSSL setup completed.

Welcome to PyServer - The Python HTTP Server!
Server Details:
IP: 0.0.0.0
Port: 80
To terminate the connection, please enter 'EXIT'.
Please be aware that certain commands may result in temporary system delays.

Server started. Press 'CTRL+C' to terminate.
```
PyServer provides a convenient way to host files and handle HTTP requests locally. It is ideal for testing web applications, APIs, and static websites. Feel free to contribute to the project and customize it to suit your specific needs.

## Code of Conduct:

We are committed to providing a welcoming and inclusive environment for all contributors. Please review our Code of Conduct before participating in this project.

## License:

This project is licensed under the MIT License. You are free to use, modify, and distribute the code in accordance with the terms of the license.

## Privacy:

PyServer does not collect or store any user data. It operates solely on your local machine and does not communicate with external servers. Your privacy and data security are important to us.

## Frequently Asked Questions (FAQ):

Can I use PyServer for production environments?
PyServer is primarily designed for testing and development purposes. It is not recommended to use it in production environments due to its limited feature set and potential security risks.

How can I serve files with PyServer?
PyServer serves files from the directory where it is executed. Simply place your files in the same directory as the PyServer script, and they will be accessible via the server.

Can I customize the server's IP address and port?
Yes, you can modify the IP address and port by editing the appropriate values in the PyServer script. However, please note that certain ports may require elevated privileges.

How can I enable SSL/HTTPS support?
You can set up SSL/HTTPS support by running PyServer with the -setup ssl command-line flag. This will install OpenSSL and enable secure connections. But currently it is not working atm!

For additional questions or support, please refer to the project's documentation or open an issue on the GitHub repository.

### Note:
Make sure to use PyServer responsibly and validate input to avoid security risks when executing commands.