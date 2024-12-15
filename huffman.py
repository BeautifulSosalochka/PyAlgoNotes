
"""
Реализован алгоритм Хаффмана с функциями для кодирования,
декодирования, тестирования и точкой входа main.
Для тестирования большого входного текста использовать файл large_text_input.txt.
"""

import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequency):
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, prefix="", codebook={}):
    if node is None:
        return

    if node.char is not None:
        codebook[node.char] = prefix

    build_huffman_codes(node.left, prefix + "0", codebook)
    build_huffman_codes(node.right, prefix + "1", codebook)

    return codebook

def huffman_encode(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    root = build_huffman_tree(frequency)
    codes = build_huffman_codes(root)

    encoded_data = ''.join(codes[char] for char in data)
    return encoded_data, codes

def huffman_decode(encoded_data, codes):
    reverse_codes = {v: k for k, v in codes.items()}
    current_code = ""
    decoded_data = []

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded_data.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_data)

def test_huffman():
    data = "this is an example for huffman encoding"
    encoded_data, codes = huffman_encode(data)
    decoded_data = huffman_decode(encoded_data, codes)

    assert data == decoded_data, "Decoded data does not match original!"

    print("Test passed!")

"""
def main():
    with open("large_text_input.txt", "r") as file:
        data = file.read()

    print("Encoding data...")
    encoded_data, codes = huffman_encode(data)

    print(f"Original size: {len(data) * 8} bits")
    print(f"Encoded size: {len(encoded_data)} bits")

    print("Decoding data...")
    decoded_data = huffman_decode(encoded_data, codes)

    assert data == decoded_data, "Decoded data does not match original."
    print("Huffman encoding and decoding completed successfully!")
"""

if __name__ == "__main__":
    test_huffman()
    #main() точка входа main предназначена для большого тестирующего текста из файла large_text.input.txt
