import numpy as np


class RSA:
    def __init__(self):
        self.P = 53
        self.Q = 59
        self.n = self.P * self.Q
        self.phi = (self.P - 1) * (self.Q - 1)
        self.e = 3
        self.d = self.__generate_d()

    def __get_random_prime(self):
        primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        return np.random.choice(primes)

    def __generate_e(self):
        for i in range(2, self.phi):
            if self.n % i != 0:
                return i
        return None

    def __generate_d(self):
        for k in range(1, self.phi):
            if (k * self.phi + 1) % self.e == 0:
                return int((k * self.phi + 1) / self.e)
        return None

    def get_public_key(self):
        return self.n, self.e

    def encrypt(self, plaintext):
        return (plaintext ** self.e) % self.n

    def decrypt(self, ciphertext):
        return (ciphertext ** self.d) % self.n


enc = RSA()
print()
print(f'Public-Key: {enc.get_public_key()}')
plaintext = 89
ciphertext = enc.encrypt(89)
print(f'Encrypted value of {plaintext}: {ciphertext}')
print(f'Decrypted value of {ciphertext}: {enc.decrypt(ciphertext)}')
print()
