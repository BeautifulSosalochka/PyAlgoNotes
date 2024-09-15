
print("\n-----LeetCode requires impl through classes-----\n")

class Solution:
    def __init__(self, words):
        self.words = words
        self.result = []
    def __getitem__(self, index):
        return self.words[index]
    def group_anagrams(self):
        anagram_dict = {}
        for i in range(len(self.words)):
            word = self[i]
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
        self.result = list(anagram_dict.values())

        print(f"Original array: {self.words}\n")
        print(f"Sorted: {self.result}")


string_arr = ["eat","tea","tan","ate","nat","bat"]


def main():
    result = Solution(string_arr)
    result.group_anagrams()


if __name__ == "__main__":
    main()