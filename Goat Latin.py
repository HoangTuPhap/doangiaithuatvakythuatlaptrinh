class Solution:
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        res = []

        for i, w in enumerate(words):
            if w[0] in vowels:
                new_word = w + "ma"
            else:
                new_word = w[1:] + w[0] + "ma"

            new_word += "a" * (i + 1)
            res.append(new_word)

        return " ".join(res)