class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def hex(self):
        hex_dict = {x: str(x) for x in range(0, 10)}
        hex_dict.update({
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f",
        })
        converted = map(lambda x: hex_dict[x//16] + hex_dict[x % 16], [self.r, self.g, self.b])
        return '#' + ''.join(converted)

    @hex.setter
    def hex(self, input):
        r, g, b = input[1:3], input[3:5], input[5:]
        self.r = int(r, 16)
        self.g = int(g, 16)
        self.b = int(b, 16)

    

c = Color(146, 255, 0)
print(c.hex)