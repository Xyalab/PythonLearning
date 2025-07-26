


class Clock:
    id = None
    price = None

    def ring(self):
        import winsound   # mac下不支持该包
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "10101"
clock1.price = 100
clock1.ring()
