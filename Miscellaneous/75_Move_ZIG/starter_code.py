#!/usr/bin/python3
import argparse
import socket

# 'argparse' is a very useful library for building python tools that are easy
# to use from the command line.  It greatly simplifies the input validation
# and "usage" prompts which really help when trying to debug your own code.
parser = argparse.ArgumentParser(description="Solver for 'All Your Base' challenge")
parser.add_argument("ip", help="IP (or hostname) of remote instance")
parser.add_argument("port", type=int, help="port for remote instance")
args = parser.parse_args();

# This tells the computer that we want a new TCP "socket"
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This says we want to connect to the given IP and port
socket.connect((args.ip, args.port))

# This gives us a file-like view of the connection which makes reading data
# easier since it handles the buffering of lines for you.
f = socket.makefile()

while True:
    line = f.readline().strip()
    print(line)
    # This iterates over data from the server a line at a time.  This can cause
    # some unexpected behavior like not seeing "prompts" until after you've sent
    # a reply for it (for example, you won't see "answer:" for this problem).
    # However, you can still send data and it will be handled correctly.

    # Handle the information from the server to extact the problem and build
    # the answer string.
    pass # Fill this in with your logic

    # Send a response back to the server
    answer = "Clearly not the answer..."
    socket.send((answer + "\n").encode()) # The "\n" is important for the server's
                                     # interpretation of your answer, so make
                                     # sure there is only one sent for each
                                     # answer.
