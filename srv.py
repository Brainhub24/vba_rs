import sys
import logging
import http.server
import socketserver

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-setup ssl":
        setup_openssl()
        return

    logger.info("Welcome to PyServer - The Python HTTP Server!")
    logger.info("Server Details:")
    logger.info("IP: 0.0.0.0")
    logger.info("Port: 80")
    logger.info("To terminate the connection, please enter 'EXIT'.")
    logger.info("Please be aware that certain commands may result in temporary system delays. If this occurs, please retry the command.")
    logger.info("")

    try:
        http_server = socketserver.TCPServer(("0.0.0.0", 80), http.server.SimpleHTTPRequestHandler)
        logger.info("Server started. Press 'CTRL+C' to terminate.")
        http_server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down the server.")
        http_server.server_close()


def setup_openssl():
    import subprocess
    import os
    import platform
    import shutil

    logger.info("Installing OpenSSL...")

    if platform.system() == "Windows":
        subprocess.run(["choco", "install", "openssl.light", "-y"], check=True)
        openssl_path = shutil.which("openssl")
        if not openssl_path:
            logger.error("Failed to find OpenSSL executable. Please make sure OpenSSL is installed correctly.")
            return
        logger.info("OpenSSL installation completed.")
    elif platform.system() == "Linux":
        try:
            subprocess.run(["sudo", "apt-get", "install", "openssl", "-y"], check=True)
            logger.info("OpenSSL installation completed.")
        except subprocess.CalledProcessError:
            logger.error("Failed to install OpenSSL. Please make sure you have the necessary permissions.")
            return
    else:
        logger.error("OpenSSL setup is currently only supported on Windows and Linux.")
        return

    logger.info("Adding OpenSSL to system PATH...")
    openssl_dir = os.path.dirname(openssl_path)
    current_path = os.environ.get("PATH", "")
    if openssl_dir not in current_path:
        new_path = f"{current_path}:{openssl_dir}"
        os.environ["PATH"] = new_path

    logger.info("OpenSSL setup completed.")


if __name__ == "__main__":
    main()
