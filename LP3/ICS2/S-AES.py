import numpy as np


def nibble_to_hex(n):
    assert len(n) <= 4, 'Invalid nibble provided.'
    if len(n) < 4:
        n = (4-len(n))*'0' + n
    return hex(int(n, 2))[2:]


def hex_to_nibble(h):
    assert len(h) == 1, 'Invalid hex digit.'
    n = bin(int(h, 16))[2:]
    return (4-len(n))*'0' + n


def block_to_state(b):
    return [
        [b[0], b[2]],
        [b[1], b[3]]
    ]


def state_to_block(s):
    return [s[0][0], s[1][0], s[0][1], s[1][1]]


def sub_nibbles(s):
    S = [
        ['9', '4', 'a', 'b'],
        ['d', '1', '8', '5'],
        ['6', '2', '0', '3'],
        ['c', 'e', 'f', '7']
    ]
    b = state_to_block(s)
    b_new = []
    for h in b:
        n = hex_to_nibble(h)
        n_new = S[int(n[:2], 2)][int(n[2:], 2)]
        b_new.append(n_new)
    return block_to_state(b_new)


def shift_rows(s):
    return [
        [s[0][0], s[0][1]],
        [s[1][1], s[1][0]]
    ]


def mul(x, y):
    p1 = [int(c) for c in hex_to_nibble(x)]
    p2 = [int(c) for c in hex_to_nibble(y)]
    return np.polymul(p1, p2)


def add(x, y):
    p = list(np.polyadd(x, y))
    p = [c % 2 for c in p]
    _, r = np.polydiv(p, [1, 0, 0, 1, 1])
    r = [str(int(c % 2)) for c in r]
    return nibble_to_hex(''.join(r))


def mix_columns(s):
    C = [
        ['1', '4'],
        ['4', '1']
    ]
    s_new = [
        [None, None],
        [None, None]
    ]
    for i in range(2):
        for j in range(2):
            s_new[i][j] = add(mul(C[i][0], s[0][j]), mul(C[i][1], s[1][j]))
    return s_new


def rot_word(w):
    return [w[1], w[0]]


def sub_word(w):
    S = [
        ['9', '4', 'a', 'b'],
        ['d', '1', '8', '5'],
        ['6', '2', '0', '3'],
        ['c', 'e', 'f', '7']
    ]
    w_new = []
    for h in w:
        n = hex_to_nibble(h)
        n_new = S[int(n[:2], 2)][int(n[2:], 2)]
        w_new.append(n_new)
    return w_new


def xor(w1, w2):
    w = []
    for i in range(2):
        x = int(hex_to_nibble(w1[i]), 2)
        y = int(hex_to_nibble(w2[i]), 2)
        w.append(nibble_to_hex(bin(x ^ y)[2:]))
    return w


def key_expansion(k):
    w0, w1 = k[:2], k[2:]
    r1 = ['8', '0']
    t2 = xor(sub_word(rot_word(w1)), r1)
    w2 = xor(w0, t2)
    w3 = xor(w1, w2)
    r2 = ['3', '0']
    t4 = xor(sub_word(rot_word(w3)), r2)
    w4 = xor(w2, t4)
    w5 = xor(w3, w4)
    return w0 + w1, w2 + w3, w4 + w5


def add_round_key(k, s):
    k_state = block_to_state(k)
    w1 = xor([k_state[0][0], k_state[1][0]], [s[0][0], s[1][0]])
    w2 = xor([k_state[0][1], k_state[1][1]], [s[0][1], s[1][1]])
    return [
        [w1[0], w2[0]],
        [w1[1], w2[1]]
    ]


def encrypt(plaintext, k):
    k1, k2, k3 = key_expansion(k)
    state = block_to_state(plaintext)
    state = add_round_key(k1, state)

    # ROUND 1
    state = sub_nibbles(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(k2, state)

    # ROUND 2
    state = sub_nibbles(state)
    state = shift_rows(state)
    state = [
        ['6', '4'],
        ['7', 'b']
    ]
    state = add_round_key(k3, state)

    ciphertext = state_to_block(state)
    return ciphertext


plaintext = ['1', 'a', '2', '3']
key = ['2', '4', '7', '5']
print()
print(f'Key : {key}')
print(f"plaintext : {plaintext}")
print(f"Encrypted plaintext is: {encrypt(plaintext, key)}")
print()
