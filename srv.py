#!/usr/bin/env python3

import logging
import socketserver

# Configuration
PORT = 80

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class CmdHttpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            # Receive data from the client
            self.data = self.request.recv(2**14).strip().decode("UTF-8")

            if len(self.data) == 0:
                return
            elif self.data.splitlines()[0].startswith("GET"):
                # Get command from user input
                command = input("%s > " % self.client_address[0]).encode("UTF-8")

                # Create response with command
                response = (
                    b"HTTP/1.1 200\ncontent-length: "
                    + str(len(command)).encode("UTF-8")
                    + b"\n\n"
                    + command
                )

                # Send response back to the client
                self.request.sendall(response)
            elif self.data.splitlines()[0].startswith("POST"):
                # Receive additional data from the client
                data = self.request.recv(2**14).strip().decode("UTF-8")
                logger.debug(data)

                # Create empty response
                response = b"HTTP/1.1 200\ncontent-length: 0\n\n"

                # Send response back to the client
                self.request.sendall(response)
                return
            else:
                logger.debug(self.data)
                # Create response indicating invalid command
                response = b"HTTP/1.1 300\ncontent-length: 0\n\n"

                # Send response back to the client
                self.request.sendall(response)
        except Exception as e:
            logger.error(f"An error occurred: {e}")


def main():
    # Initialize logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    logger.info("To terminate the connection, please enter 'EXIT'.")
    logger.info("Please be aware that certain commands may result in temporary system delays. If this occurs, please retry the command.")
    logger.info("")

    try:
        # Start the server
        with socketserver.TCPServer(("0.0.0.0", PORT), CmdHttpHandler) as server:
            server.serve_forever()
    except Exception as e:
        logger.error(f"Server error occurred: {e}")


if __name__ == "__main__":
    main()
