def log(type : int, msg : str) -> None:
    """
    type = 0: ok.
    type = 1: Not found.
    type = 2: Invalid params.
    type = 3: Already exists.
    """
    if type == 0:
        print("[+] " + msg) # Ok message.
    if type == 1:
        print("[*] ERROR: " + msg + " Not found.") # Error
        exit(1)
    if type == 2:
        print("[-] COMMAND ERROR: `" + msg + "` Invalid params.") # Error
        exit(1)
    if type == 3:
        print("[-] ERROR: " + msg + " Already exists.") # Error
        exit(1)