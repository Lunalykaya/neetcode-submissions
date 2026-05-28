class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
          if len(s) != len(t):
            return False
          letter = list(s)
          for n in t:
            if n in letter:
                letter.remove(n)
          return len(letter) == 0