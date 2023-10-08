from cryptography.fernet import Fernet

# 生成随机密钥
key = Fernet.generate_key()

# 创建Fernet对象
cipher_suite = Fernet(key)

# 要加密的明文
message = b"Hello, World!"

# 加密明文
ciphertext = cipher_suite.encrypt(message)
print("密文:", ciphertext)

# 解密密文
decrypted_message = cipher_suite.decrypt(ciphertext)
print("解密后的明文:", decrypted_message)
