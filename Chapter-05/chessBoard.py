def isValidChessBoard(my_dict):
    valid = True
    count = 0
    my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    if (len(my_dict.keys()) > 32):
        valid = False

    for keys in my_dict:
        if (int(keys[0]) > 8 and keys[1] not in my_list):
            valid = False
            break

    for values in my_dict.values():
        if (values[0] not in ['b', 'w']):
            valid = False
            break
        if (values in ['wking', 'bking']):
            count += 1

    if (valid and count == 2):
        return True
    else:
        return False


my_dict = {'1h': 'bking', '6c': 'wqueen',
           '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(my_dict))
