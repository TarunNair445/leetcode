class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reversed_t = words[::-1]
        result = " ".join(reversed_t)

        return result

        