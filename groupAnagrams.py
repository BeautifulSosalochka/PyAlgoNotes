
class Solution:
    """
    doctest a class to group anagrams from a list of words.
        Attributes:
        words: List of words provided as input.
        result: List that stores grouped anagrams.
    >>> words = ["eat","tea","tan","ate","nat","bat"]
    >>> result = Solution(words)
    >>> result.group_anagrams()
    Original array: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    Sorted: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    """
    def __init__(self, words: list[str]) -> None:
        self.words: list[str] = words
        self.result: list[list[str]] = []
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

        print(f"Original array: {self.words}")
        print(f"Sorted: {self.result}")


string_arr = ["eat","tea","tan","ate","nat","bat"]


def main():
    result = Solution(string_arr)
    result.group_anagrams()


if __name__ == "__main__":
    main()