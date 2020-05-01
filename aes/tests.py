import unittest
import aes


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.key = [
            0x2b, 0x7e, 0x15, 0x16,
            0x28, 0xae, 0xd2, 0xa6,
            0xab, 0xf7, 0x15, 0x88,
            0x09, 0xcf, 0x4f, 0x3c,
        ]
        self.plaintext = [
            0x32, 0x43, 0xf6, 0xa8,
            0x88, 0x5a, 0x30, 0x8d,
            0x31, 0x31, 0x98, 0xa2,
            0xe0, 0x37, 0x07, 0x34,
        ]
        self.ciphertext = [
            0x39, 0x25, 0x84, 0x1d,
            0x02, 0xdc, 0x09, 0xfb,
            0xdc, 0x11, 0x85, 0x97,
            0x19, 0x6a, 0x0b, 0x32,
        ]
        self.aes = aes.AES(self.key)

    def test_RotWord(self):
        result = aes.RotWord([0, 1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 0])

    def test_SubBytes(self):
        result = aes.SubBytes([0x19, 0x3d, 0xe3, 0xbe])
        self.assertEqual(result, [0xd4, 0x27, 0x11, 0xae])

    def test_XorBytes(self):
        result1 = aes.XorBytes([0x28, 0xae, 0xd2, 0xa6],
                              [0xa0, 0xfa, 0xfe, 0x17])
        self.assertEqual(result1, [0x88, 0x54, 0x2c, 0xb1])

        result2 = aes.XorBytes([0x2b, 0x7e, 0x15, 0x16],
                              [0x8a, 0x84, 0xeb, 0x01],
                              [0x01, 0x00, 0x00, 0x00])
        self.assertEqual(result2, [0xa0, 0xfa, 0xfe, 0x17])

    def test_Rcon(self):
        result = aes.Rcon(0)
        self.assertEqual(result, [1, 0, 0, 0])

    def test_GenerateRoundKeys(self):
        result = aes.GenerateRoundKeys(self.key)
        expected = [208, 20, 249, 168, 201, 238, 37, 137,
                    225, 63, 12, 200, 182, 99, 12, 166]
        self.assertEqual(result[-16:], expected)

    def test_MixColumns(self):
        expected = [208, 20, 249, 168, 201, 238, 37, 137,
                    225, 63, 12, 200, 182, 99, 12, 166]
        self.aes.State = expected
        self.aes.MixColumns()
        self.aes.MixColumns(inv=True)
        self.assertEqual(expected, self.aes.State)

    def test_ShiftRows(self):
        expected = [208, 20, 249, 168, 201, 238, 37, 137,
                    225, 63, 12, 200, 182, 99, 12, 166]
        self.aes.State = expected
        self.aes.ShiftRows()
        self.aes.ShiftRows(inv=True)
        self.assertEqual(expected, self.aes.State)

    def test_encrypt16bytes(self):
        result = self.aes.encrypt16bytes(self.plaintext)
        self.assertEqual(self.ciphertext, result)

    def test_decrypt16bytes(self):
        result = self.aes.decrypt16bytes(self.ciphertext[:])
        self.assertEqual(self.plaintext, result)


if __name__ == '__main__':
    unittest.main()
