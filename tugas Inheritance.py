class Robot(object):
    def __init__(self, micro, motor, baterai):
        self.micro = micro
        self.motor = motor
        self.baterai = baterai

    def komponen(self):
        print("microcontroller\t: ",self.micro)
        print("motor\t: ",self.motor)
        print("baterai\t: ",self.baterai)

class transpoter(Robot):
    def __init__(self,micro,motor,baterai,capit):
        self.micro = micro
        self.motor = motor
        self.baterai = baterai
        self.capit = capit

    def listkomponen(self):
        print("jumlah microcontroller\t: ",self.micro)
        print("jumlah motor\t: ",self.motor)
        print("jumlah baterai\t: ",self.baterai)
        print("jumlah capit\t: ",self.capit)


robottranspoter = transpoter('arduino','motor DC','lippo','2 buah')

robottranspoter.komponen()
robottranspoter.listkomponen()

