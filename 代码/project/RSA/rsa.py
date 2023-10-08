import random


def generate_keys(p, q):
    # 计算 n = p * q 和 φ(n) = (p-1) * (q-1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # 选择公钥指数 e，满足 1 < e < φ(n) 且 e 与 φ(n) 互质
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # 计算私钥指数 d，满足 e * d ≡ 1 (mod φ(n))
    d = modular_inverse(e, phi)

    # 返回公钥和私钥
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y


def modular_inverse(a, m):
    d, x, y = extended_gcd(a, m)
    if d == 1:
        return x % m
    else:
        raise ValueError("The modular inverse does not exist.")


def encrypt(message, public_key):
    n, e = public_key
    # 加密明文 m，计算密文 c = m^e (mod n)
    ciphertext = pow(message, e, n)
    return ciphertext


def decrypt(ciphertext, private_key):
    n, d = private_key
    # 解密密文 c，计算明文 m = c^d (mod n)
    message = pow(ciphertext, d, n)
    return message


# 示例用法
p = 61  # 第一个大素数
q = 53  # 第二个大素数

public_key, private_key = generate_keys(p, q)

message = 123  # 要加密的明文

# 加密
ciphertext = encrypt(message, public_key)
print("密文:", ciphertext)

# 解密
decrypted_message = decrypt(ciphertext, private_key)
print("解密后的明文:", decrypted_message)