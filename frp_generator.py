import sys


def gui_handler():
    print("We are currently not supporting GUI yet!")
    exit()


if __name__ == "__main__":
    argv = sys.argv

    # mode = 0 for create mode
    # mode = 1 for append mode
    mode = 0

    # gui = 0 for not using gui
    # gui = 1 for using gui
    gui = 0

    # verbose = 0 for not using verbose mode
    # verbose = 1 for using verbose mode
    verbose = 0

    local_ip = ""

    server_ip = ""
    # server_port = -1 for a invalid port
    server_port = -1

    port_list = {}

    filename = ""

    for i in range(len(argv)):
        # append
        if argv[i] == "-a" or argv[i] == "--append":
            mode = 1
            if argv[i + 1].find("-") == -1:
                # The user specifies a filename
                filename = argv[i + 1]

        # gui
        if argv[i] == "-g" or argv[i] == "--gui":
            gui = 1
            gui_handler()

        # local ip
        if argv[i] == "-l" or argv[i] == "--local_ip":
            local_ip = argv[i + 1]

        # server ip
        if argv[i] == "-s" or argv[i] == "--server_ip":
            if argv[i + 1].find(":") != -1:
                # The address does contains a port
                ip_port = argv[i + 1].split(":")
                print(ip_port)
                server_ip = ip_port[0]
                server_port = ip_port[1]
            else:
                print("Error: -s parameter should followed by both ip address and port")
                print("For example: -s 8.8.8.8:80")
                print("Invalid Input, Aborting!")
                exit()

        # port
        if argv[i] == "-p" or argv[i + 1] == "--port":
            if argv[i + 1].find("->") != -1:
                # The user specifies a port translation
                pass
            elif argv[i + 1].find("-") != -1:
                # The user specifies a port range
                pass
            else:
                # The user specifies a normal port
                pass

        # verbose
        if argv[i] == "-v" or argv[i] == "-verbose":
            verbose = 1

    if verbose:
        print("Mode:", mode)
        print("GUI:", gui)
        print("Verbose:", verbose)
        print("Local IP:", local_ip)
        print("Server IP:", server_ip)
        print("Server Port", server_port)
        print("Port List:", port_list)
        print("Filename:", filename)

