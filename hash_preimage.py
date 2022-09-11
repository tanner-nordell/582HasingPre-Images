import hashlib
import os

def hash_preimage(target_string):
    if not all( [x in '01' for x in target_string ] ):
        print( "Input should be a string of bits" )
        return

    num_bits = len(target_string)
    print("num_bits = ", num_bits);
    target_int = int(target_string, 2)

    mask = (1<<num_bits)-1
    size = 16
    x = os.urandom(size)
    while(1):
        x = os.urandom(size) #create
        x_hashed = hashlib.sha256(x)
        x_last_few_bits = int(x_hashed.hexdigest(), 16) & mask
        if (x_last_few_bits == target_int):
            break

    print("x in hex: " + x.hex())
    print("target_string/int in hex: ", hex(target_int))
    print("h(x) = ", x_hashed.hexdigest(), "  h(x) last", num_bits ,"bits in hex:", hex(x_last_few_bits))

    nonce = x
    #nonce = b'\x00'

    return( nonce )

