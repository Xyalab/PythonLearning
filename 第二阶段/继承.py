
class Phone:
    model = "Mate50 Pro"
    year = None
    network = "4G"

    def __init__(self):
        self.year = 2023

    def calling(self):
        print(f'{self.network}网络通话中')


class NewPhone(Phone):
    network = "5G"

    def __init__(self, network):
        self.model = "Mate60 Pro"
        self.year = 2024
        self.network = network

    def calling(self):
        print(f'{self.network}网络通话中')
        print(f"老款手机型号是{super().model}, 网络制式为{super().network}")
        print(f"老款手机型号是{Phone.model}, 网络制式为{Phone.network}")

new_phone = NewPhone("卫星")
new_phone.calling()



class NFC:
    def nfc(self):
        print("刷NFC")


class NewNewPhone(Phone, NFC):
    pass   # 继承父类后，不再有其他操作，避免语法问题，可以使用pass


new_phone1 = NewNewPhone()
new_phone1.nfc()
new_phone1.network = "5G"
new_phone1.calling()