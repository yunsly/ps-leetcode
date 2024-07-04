# Sol1 : 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # check vaildity of string
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # check Palindrome or not
        while len(strs) > 1:
            if strs.pop(0) != strs.pop() :
                return False
        return True

# -----------------------------------------------
# Sol2 : Deque 사용
import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # check vaildity of string
        strs :Deque = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        # check Palindrome or not
        while len(strs) > 1:
            if strs.popleft() != strs.pop() :
                return False
        return True

# -----------------------------------------------
# Sol3 : 정규식 + 슬라이싱 사용

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        # filtering
        s = re.sub('[^a-z0-9]','',s)
        return s == s[::-1]