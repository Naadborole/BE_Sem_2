class S_DES:
    def __init__(self, key: int):
        assert key > 0 and key <= 1023, "The key must be between 0 and 1023"
        self.key = key
        self.key_bt = "{0:b}".format(key)
        self.key_bt = '0'*(10 - len(self.key_bt)) + self.key_bt

    def P10(self, key):
        m = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def IP(self, key):
        m = [2, 6, 3, 1, 4, 8, 5, 7]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def IPInverse(self, key):
        m = [4,1,3,5,7,2,8,6]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def LS(self, key, times):
        t= key
        for i in range(times):
            t = t[1:] + t[0]
        return t

    def P8(self, key):
        m = [6, 3, 7, 4, 8, 5, 10, 9]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def P4(self, key):
        m = [2, 4, 3, 1]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def EP(self, key):
        m = [4, 1, 2, 3, 2, 3, 4, 1]
        t = ''
        for i in m:
            t += key[i-1]
        return t

    def S0(self, key):
        s0 = [['01', '00', '11', '10'], ['11', '10', '01', '00'], ['00', '10', '01', '11'], ['11', '01', '11', '10']]
        return s0[int(str(key[0] + key[3]), 2)][int(str(key[1] + key[2]),2)]

    def S1(self, key):
        s1 = [['00', '01', '10', '11'], ['10', '00', '01', '11'], ['11', '00', '01', '00'], ['10', '01', '00', '11']]
        return s1[int(str(key[0] + key[3]), 2)][int(str(key[1] + key[2]),2)]

    def GenerateKeys(self):
        p10 = self.P10(self.key_bt)
        self.k1 = self.P8(self.LS(p10[:5],1) + self.LS(p10[5:],1))
        self.k2 = self.P8(self.LS(p10[:5],3) + self.LS(p10[5:],3))

    def RoundFunction(self, inp,k):
        t = self.EP(inp[4:])
        t = "{0:b}".format((int(k,2)^int(t,2)))
        t = '0'*(8-len(t)) + t
        t = self.S0(t[:4]) + self.S1(t[4:])
        t = self.P4(t)
        t = "{0:b}".format((int(inp[:4],2)^int(t,2)))
        t = '0'*(4-len(t)) + t
        return t + inp[4:]

    def Encrypt(self, inp):
        assert inp>0 and inp <= 255, "The input value must be 8 bit i.e. between 0 and 255"
        self.GenerateKeys()
        inp = "{0:b}".format(inp)
        inp = '0'*(8 - len(inp)) + inp 
        t = self.IP(inp)
        t = self.RoundFunction(t,self.k1)
        t = t[4:] + t[:4]
        t = self.RoundFunction(t, self.k2)
        t = self.IPInverse(t)
        return t


if __name__ == "__main__":
    print()
    inp = "{0:b}".format(114)
    inp = '0'*(8 - len(inp)) + inp 
    key_bt = "{0:b}".format(642)
    key_bt = '0'*(10 - len(key_bt)) + key_bt
    print("---------------------------S-DES---------------------------")
    print(f'Input: {inp} ({114})')
    print(f'Key : {key_bt} ({642})')
    print("-----------------------------------------------------------")
    sdes = S_DES(642)
    sdes.GenerateKeys()
    print(f'K1 : {sdes.k1}')
    print(f'K2 : {sdes.k2}')
    print()
    t = sdes.Encrypt(114)
    print(f'Cipher: {t}')
    print("-----------------------------------------------------------")
    print()

