class ECC:
  def __init__(self, a, b, q, G):
    ### CURVE EQUATION = x ** 3 + a * x + b
    self.a = a
    self.b = b
    self.q = q
    self.G = G
    self.private_key = 5
    self.public_key = self.__generate_public_key()

  def __round(self, p):
    x, y = p
    if abs(x - int(x)) <= 0.0001: x = int(x)
    if abs(y - int(y)) <= 0.0001: y = int(y)
    return (x, y)
  
  def negate(self, p):
    return (p[0], -p[1])

  def add(self, p1, p2):
    if p1 == p2:
      x = ((3*p1[0]*p1[0] + self.a)/(2*p1[1]))**2 - 2*p1[0]
      y = -p1[1] + (3*p1[0]*p1[0] + self.a)/(2*p1[1]) * (p1[0] - x)
    else:
      x = ((p2[1]-p1[1])/(p2[0]-p1[0]))**2 - p1[0] - p2[0]
      y = -p1[1] + (p2[1]-p1[1])/(p2[0]-p1[0]) * (p1[0]-x)
    return self.__round((x, y))

  def sub(self, p1, p2):
    return self.add(p1, self.negate(p2))

  def dot(self, k, p):
    res = (p[0], p[1])
    for _ in range(k-1):
      res = self.add(res, p)
      res = self.negate(res)
    return res

  def __generate_public_key(self):
    return self.dot(self.private_key, self.G)

  def get_public_key(self):
    return self.public_key

  def generate_secret_key(self, public_key):
    self.secret_key = self.dot(self.private_key, public_key)

  def encrypt(self, message, public_key):
    k = 3
    return (self.dot(k, G), self.add(message, self.dot(k, public_key)))

  def decrypt(self, message):
    return self.sub(message[1], self.dot(self.private_key, message[0]))
print()
a = 1
b = 6
q = 11
G = (5, 2)
ecc = ECC(a, b, q, G)
private_key = 8
public_key = ecc.dot(private_key, G)
print(f'PUBLIC-KEY: {public_key}')
ecc.generate_secret_key(public_key)
secret_key = ecc.dot(private_key, ecc.get_public_key())
print(f'SECRET-KEY: {secret_key}')
message = (2, 7)
ciphertext = ecc.encrypt(message, public_key)
print(f'MESSAGE: {message}\nCIPHERTEXT: {ciphertext}')
decrypted_text = ecc.sub(ciphertext[1], ecc.dot(private_key, ciphertext[0]))
print(f'DECRYPTED-TEXT: {decrypted_text}')
print()