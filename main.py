from machine import Pin



num = int(input("Enter a base 8 number: "))
if num < 0 or num > 7:
    raise ValueError("Input must be between 0 and 7")

bin_str = bin(num)[2:]
while len(bin_str) < 3:
    bin_str = '0' + bin_str

binary_tuple = tuple(int(i) for i in bin_str)

numR = num - 2
bin_strR = bin(numR)[2:]
while len(bin_strR) < 3:
    bin_strR = '0' + bin_strR


a = Pin(17, Pin.OUT)
b = Pin(18, Pin.OUT)
c = Pin(20, Pin.OUT)


a.value(binary_tuple[0])
b.value(binary_tuple[1])
c.value(binary_tuple[2])