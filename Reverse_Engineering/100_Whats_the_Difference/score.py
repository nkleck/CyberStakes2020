'''

LPWSTR FUN_0060d000(void)

{
  ushort local_54 [32];
  LPWSTR local_14;
  int local_10;

  local_14 = GetCommandLineW();
  local_10 = 0;
  while( true ) {
    if (0x1f < local_10) {
      MessageBoxW((HWND)0x0,local_14 + 0x32,(LPCWSTR)local_54,0);
      return local_14;
    }
    if ((ushort)(local_14[local_10 + 0x32] ^ u_6ddf63053B391EB898A2EeFBADb0De3d_0060d180[local_10])
        != *(ushort *)(&DAT_0060d0c0 + local_10 * 2)) break;
    local_54[local_10] =
         *(ushort *)(&DAT_0060d120 + local_10 * 2) ^
         u_6ddf63053B391EB898A2EeFBADb0De3d_0060d180[local_10];
    local_10 = local_10 + 1;
  }
  return local_14;
}


x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.

'''

import binascii
import base64

# we need INTs for the exclusive xor
# so we will conver these hex strings to int below
# then we exclusive xor
DAT_0060d0c0_hex = ["77", "27", "2D", "1D", "53", "56", "54", "04", "05", "7A", "51", "08", "57", "21", "75", "5D", "01", "08", "75", "53", "72", "52", "7F", "70", "73", "22", "04", "02", "76", "55", "00", "19"]
DAT_0060d120_hex = ["78", "0B", "10", "46", "54", "52", "54", "1E", "18", "62", "47", "51", "54", "65", "24", "54", "58", "5F", "61", "5B", "36", "5F", "66", "62", "61", "64", "42", "10", "64", "45", "13", "44"]
# DAT_0060d120_ints = [120, 11, 16, 70, 84, 82, 84, 30, 24, 98, 71, 81, 84, 101, 36, 84, 88, 95, 97, 91, 54, 95, 102, 98, 97, 100, 66, 16, 100, 69, 19, 68]

# turing this unicode into a list 6ddf63053B391EB898A2EeFBADb0De3d
unicode_hex1 = ["36", "64", "64", "66", "36", "33", "30", "35", "33", "42", "33", "39", "31", "45", "42", "38", "39", "38", "41", "32", "45", "65", "46", "42", "41", "44", "62", "30", "44", "65", "33", "64"]
# i used rapidtables to convert ascii to hex
unicode_ints = [54, 100, 100, 102, 54, 51, 48, 53, 51, 66, 51, 57, 49, 69, 66, 56, 57, 56, 65, 50, 69, 101, 70, 66, 65, 68, 98, 48, 68, 101, 51, 100]


# convert DAT_0060d0c0_hex to ints
DAT_0060d0c0_ints = []
for item in DAT_0060d0c0_hex:
    x = int(item, 16)
    DAT_0060d0c0_ints.append(x)

# convert DAT_0060d120_hex to int
DAT_0060d120_ints = []
for item in DAT_0060d120_hex:
    x = int(item, 16)
    DAT_0060d120_ints.append(x)


def dec_to_raw(source_data):
    # convert dec to hex
    myhex = hex(int(source_data))[2:]
    # convert hex to base64
    mybase64 = binascii.b2a_base64(binascii.unhexlify(myhex)).decode().replace("\n", "")
    # convert base64 to raw
    return(binascii.a2b_base64(mybase64).decode())

local_14 = []
local_54 = []
count = 0
while True:
    if count > 31:
        break

    # xor the two data sections against the unicode string
    local_14.append(DAT_0060d0c0_ints[count] ^ unicode_ints[count])
    local_54.append(DAT_0060d120_ints[count] ^ unicode_ints[count])

    # increment
    count = count + 1
    print(local_14)
    print(local_54)

# now lets convert local_54 to something
local_54_str = ""
for item in local_54:
    local_54_str += dec_to_raw(item)

local_14_str = ""
for item in local_14:
    local_14_str += dec_to_raw(item)

print("{}{}".format(local_54_str, local_14_str))
