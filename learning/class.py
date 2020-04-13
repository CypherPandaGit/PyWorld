

class Computer:

    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def config(self):
        print(f'Configuration is: {self.cpu}, {self.ram}GB RAM and {self.hdd}TB SSD.')


computer_1 = Computer('Ryzen 5', 32, 1)
computer_2 = Computer('i7', 16, 1)

computer_1.config()

computer_2.config()
