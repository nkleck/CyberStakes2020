#!/usr/bin/python3
import binascii
import base64
import socket
import time

ip = "challenge.acictf.com"
port = 32264

# ------------------------------------------------------------------------------
# XXX TO RAW
# ------------------------------------------------------------------------------
def dec_to_raw(source_data):
    # convert dec to hex
    myhex = hex(int(source_data))[2:]
    # convert hex to base64
    mybase64 = binascii.b2a_base64(binascii.unhexlify(myhex)).decode().replace("\n", "")
    # convert base64 to raw
    return(binascii.a2b_base64(mybase64).decode())


def oct_to_raw(source_data):
    # convert oct to decimal
    mydec = str(int(source_data, 8))
    # convert dec to hex
    myhex = hex(int(mydec))[2:]
    # convert hex to base64
    mybase64 = binascii.b2a_base64(binascii.unhexlify(myhex)).decode().replace("\n", "")
    # convert base64 to raw
    return(binascii.a2b_base64(mybase64).decode())


def bin_to_raw(source_data):
    # convert bin to dec
    mydec1 = int(source_data, 2)
    # convert int to hex
    myhex = hex(mydec1)[2:]
    # convert hex to base64
    mybase64 = binascii.b2a_base64(binascii.unhexlify(myhex)).decode().replace("\n", "")
    # convert base64 to raw
    return(binascii.a2b_base64(mybase64).decode())


def hex_to_raw(source_data):
    # convert hex to base64
    mybase64 = binascii.b2a_base64(binascii.unhexlify(source_data)).decode().replace("\n", "")
    # convert base64 to raw
    return(binascii.a2b_base64(mybase64).decode())


def b64_to_raw(source_data):
    # convert base64 to raw
    return(binascii.a2b_base64(source_data).decode())


# ------------------------------------------------------------------------------
# RAW TO ANSWER
# ------------------------------------------------------------------------------
def raw_to_dec(raw_data):
    # convert raw to b64
    myb64 = binascii.b2a_base64(raw_data.encode()).decode().replace("\n", "")
    # convert base64 to hex
    myhex = base64.b64decode(myb64).hex()
    # convert hex to dec
    return(int(myhex, 16))


def raw_to_oct(raw_data):
    # convert raw to b64
    myb64 = binascii.b2a_base64(raw_data.encode()).decode().replace("\n", "")
    # convert base64 to hex
    myhex = base64.b64decode(myb64).hex()
    # convert hex to dec
    i = int(myhex, 16)
    # convert dec to oct
    return(oct(i)[2:])


def raw_to_bin(raw_data):
    # convert raw to b64
    myb64 = binascii.b2a_base64(raw_data.encode()).decode().replace("\n", "")
    # convert base64 to hex
    hex_string = base64.b64decode(myb64).hex()
    # convert hex to binary (1 and 0)
    return(bin(int(hex_string, 16))[2:])


def raw_to_hex(raw_data):
    # convert raw to b64
    myb64 = binascii.b2a_base64(raw_data.encode()).decode().replace("\n", "")
    # convert base64 to hex
    return(base64.b64decode(myb64).hex())


def raw_to_b64(raw_data):
    # convert raw to b64
    return(binascii.b2a_base64(raw_data.encode()).decode().replace("\n", ""))


def get_raw_data(src_encoding, source_data):
    if src_encoding == 'dec':
        raw_data = dec_to_raw(source_data)
    elif src_encoding == 'oct':
        raw_data = oct_to_raw(source_data)
    elif src_encoding == 'bin':
        raw_data = bin_to_raw(source_data)
    elif src_encoding == 'hex':
        raw_data = hex_to_raw(source_data)
    elif src_encoding == 'b64':
        raw_data = b64_to_raw(source_data)
    else:
        raw_data = source_data
    return raw_data


def get_answer(dst_encoding, raw_data):
    if dst_encoding == 'dec':
        answer = raw_to_dec(raw_data)
    elif dst_encoding == 'oct':
        answer = raw_to_oct(raw_data)
    elif dst_encoding == 'bin':
        answer = raw_to_bin(raw_data)
    elif dst_encoding == 'hex':
        answer = raw_to_hex(raw_data)
    elif dst_encoding == 'b64':
        answer = raw_to_b64(raw_data)
    else:
        answer = raw_data
    return answer


# This tells the computer that we want a new TCP "socket"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# This says we want to connect to the given IP and port
sock.connect((ip, port))
# sock.setblocking(0)
# make socket easy to read
f = sock.makefile()

acc_list = ['raw', 'b64', 'hex', 'dec', 'oct', 'bin']

count = 0
while True:
    line = f.readline().strip()
    print(line)
    # if not line:
    #     break
    # This iterates over data from the server a line at a time.  This can
    # cause some unexpected behavior like not seeing "prompts" until after
    # you've sent a reply for it (for example, you won't see "answer:" for
    # this problem). However, you can still "sock.send" below to transmit data
    # and the server will handle it correctly.

    # Handle the information from the server to extact the problem and build
    # the answer string.
    # pass # Fill this in with your logic
    if ' -> ' in line:
        enc_lst = line.split(' -> ')
        if enc_lst[0] in acc_list:
            # print(enc_lst)
            src_encoding = enc_lst[0]
            dst_encoding = enc_lst[1]
            source_data = f.readline().strip()
            # print("Translate SRC {} {} to {}".format(src_encoding, source_data, dst_encoding))
            # get raw data from source encoding
            raw_data = get_raw_data(src_encoding, source_data)
            # get answer from raw dta
            answer = get_answer(dst_encoding, raw_data)

            # Send a response back to the server
            # print("Answer: {}".format(answer))
            time.sleep(.2)
            # answer = "Clearly not the answer..."
            sock.send(("{}\n".format(answer)).encode())
            # print(count)
            # count = count +1
sock.close()
