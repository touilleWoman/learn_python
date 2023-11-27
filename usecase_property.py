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


c = Color(146, 255, 0)
print(c.hex)