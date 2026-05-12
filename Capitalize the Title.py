class Solution:
    def capitalizeTitle(self, title):
        words = title.split()
        res = []

        for word in words:
            word = word.lower()

            if len(word) <= 2:
                res.append(word)
            else:
                res.append(word[0].upper() + word[1:])

        return " ".join(res)