'''
rotor 模块

这个模块在 2.3 时被声明不赞成, 2.4 时废了. 因为它的加密算法不安全.
'''
'''
# 使用 rotor 模块
import rotor


SECRET_KEY = "spam"
MESSAGE = "the holy grail"

r = rotor.newrotor(SECRET_KEY)

encoded_message = r.encrypt(MESSAGE)
decoded_message = r.decrypt(encoded_message)

print("original:", repr(MESSAGE))
print("encoded message:", repr(encoded_message))
print("decoded message:", repr(decoded_message))
'''