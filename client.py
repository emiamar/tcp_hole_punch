import socket
import utils


def main(host='54.187.46.146', port=5005):
    randevous_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    randevous_server_socket.setsockopt(
        socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    randevous_server_socket.connect((host, port))
    private_address = randevous_server_socket.getsockname()
    print("My Private Address {}".private_address)
    utils.send_msg(
        randevous_server_socket,
        utils.addr_to_msg(private_address)
    )


if __name__ == '__main__':
    main()
