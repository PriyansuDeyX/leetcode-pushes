1class Solution:
2
3  def numOfStrings(self, patterns: List[str], word: str) -> int:
4    return sum(p in word for p in patterns)