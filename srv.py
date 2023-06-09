import socketserver
import logging
from http.client import HTTPMessage
from email import message_from_string

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Server settings
HOST = "0.0.0.0"
PORT = 80


class CmdHttpHandler(socketserver.StreamRequestHandler):
    def handle(self):
        try:
            # Get client address
            client_ip, client_port = self.client_address

            # Log client connection
            logger.info("Client connected from %s:%s", client_ip, client_port)

            # Receive data from the client
            self.data = self.rfile.read(2 ** 14).strip().decode("UTF-8")

            if len(self.data) == 0:
                return

            # Parse the HTTP request headers
            headers, body = self.data.split("\r\n\r\n", 1)
            headers_dict = dict(
                map(str.strip, header.split(":", 1)) for header in headers.split("\r\n")[1:]
            )

            # Get User-Agent header
            user_agent_header = headers_dict.get("User-Agent")
            user_agent = HTTPMessage()
            user_agent.add_header("User-Agent", user_agent_header)
            user_agent_info = dict(user_agent.items())

            logger.info("Browser details:")
            for key, value in user_agent_info.items():
                logger.info("%s: %s", key, value)

            if self.data.splitlines()[0].startswith("GET"):
                # Get command from user input
                command = input("%s > " % client_ip).encode("UTF-8")

                # Create response with command
                response = (
                    b"HTTP/1.1 200\ncontent-length: "
                    + str(len(command)).encode("UTF-8")
                    + b"\n\n"
                    + command
                )

                # Send response back to the client
                self.wfile.write(response)
            elif self.data.splitlines()[0].startswith("POST"):
                # Receive additional data from the client
                data = self.rfile.read(2 ** 14).strip().decode("UTF-8")
                logger.debug(data)

                # Create empty response
                response = b"HTTP/1.1 200\ncontent-length: 0\n\n"

                # Send response back to the client
                self.wfile.write(response)
                return
            else:
                logger.debug(self.data)
                # Create response indicating invalid command
                response = b"HTTP/1.1 300\ncontent-length: 0\n\n"

                # Send response back to the client
                self.wfile.write(response)
        except Exception as e:
            logger.error(f"An error occurred: {e}")


def main():
    logger.info("Welcome to the Simple HTTP Server!")
    logger.info("Server Details:")
    logger.info("IP: %s", HOST)
    logger.info("Port: %s", PORT)
    logger.info("To terminate the connection, please enter 'EXIT'.")
    logger.info("Please be aware that certain commands may result in temporary system delays. If this occurs, please retry the command.")
    logger.info("")

    # Create the server
    with socketserver.TCPServer((HOST, PORT), CmdHttpHandler) as server:
        logger.info("Waiting for incoming connections...")
        server.serve_forever()


if __name__ == "__main__":
    main()
