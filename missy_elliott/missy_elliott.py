class MissyElliott(object):

    def encode(self, encode_str):
        str_vals = [ord(x) for x in encode_str]
        binify = [bin(x)[2:].zfill(8) for x in str_vals]
        shift_bits = [self.shift_it(x, 1) for x in binify]
        flipped_and_reversed = [self.flip_it(x)[::-1] for x in shift_bits]
        return ''.join([hex(int(x, 2)) for x in flipped_and_reversed])

    def decode(self, decode_str):
        split_input = [decode_str[i:i+4] for i in range(0, len(decode_str), 4)]
        split_hex = [hex(int(x, 16)) for x in split_input]
        unbinify = [bin(int(x, 16))[2:].zfill(8) for x in split_hex]
        reversed_and_flipped = [self.flip_it(x)[::-1] for x in unbinify]
        shift_bits = [self.shift_it(x, -1) for x in reversed_and_flipped]
        return ''.join([chr(int(x, 2)) for x in shift_bits])

    def shift_it(self, unshifted, shift_val):
        return unshifted[shift_val:]+ unshifted[:shift_val]

    def flip_it(self, bits):
        return ''.join('1' if x == '0' else '0' for x in bits)