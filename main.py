# # 파이썬 패키지
# from MyApp.Handlers.text_handler import handle_text
#
# input_text = "python_basic package practice"
# handle_text(input_text)
import collections


# 변환된 텍스트: PYTHON_BASIC PACKAGE PRACTICE

# # 기본 예외처리
# try:
#     # result = 10 / 0 # for ZeroDivisionError
#     # number = int("Not a number") # for ValueError
#     number = 5 + "Not a number"
# except ZeroDivisionError:
#     print("Error: Division by zero.")
# # Error: Division by zero.
# except ValueError:
#     print("Error: Invalid value.")
# # Error: Division by zero.
# except TypeError:
#     print("Error: Invalid type.")
# # Error: Invalid type.
#
# print("Program continues.")
# # Program continues.

# # custom exception
# class CustomException(Exception):
#     def __init__(self, message):
#         self.message = message
#
# try:
#     raise CustomException("This is a custom exception.")
# except CustomException as e:
#     print(f"Error: {e.message}")

# # 파이썬 알고리즘
# a = ['a1', 'b2', 'c3']
#
# # 방법 1: range 사용
# for i in range(len(a)):
#     print(i, a[i])
# # 0 a1
# # 1 b2
# # 2 c3
#
# # 방법 2: 직관적인 방법
# i = 0
# for v in a:
#     print(i, v)
#     i += 1
# # 0 a1
# # 1 b2
# # 2 c3
#
# # 방법 3: enumerate
# for i, v in enumerate(a):
#     print(i, v)
# # 0 a1
# # 1 b2
# # 2 c3

# # 리스트 메서드의 시간 복잡도
# len(a) # 시간 복잡도 : O(1) - 전체 요소의 개수를 리턴한다.
# a[i] # 시간 복잡도 : O(1) - 인덱스 i의 요소를 가져온다.
# a[i:j] # 시간 복잡도 : O(k) - 인덱스 i 부터 j 까지 슬라이스의 길이만큼인 k 개의 요소를 가져온다. 이 경우 객체 1개에 대한 조회가 필요하므로 O(k) 이다.
# elem in a # 시간 복잡도 : O(n) - elem 요소가 존재하는지 확인한다. 처음부터 순차 탐색하므로 n 만큼 시간이 소요된다.
# a.count(elem) # 시간 복잡도 : O(n) - elem 요소의 개수를 리턴한다.
# a.index(elem) # 시간 복잡도 : O(n) - elem 요소의 인덱스를 리턴한다.
# a.append(elem) # 시간 복잡도 : O(1) - 리스트 마지막에 elem 요소를 추가한다.
# a.pop() # 시간 복잡도 : O(1) - 리스트 마지막 요소를 추출한다. 스택의 연산이다.
# a.pop(0) # 시간 복잡도 : O(n) - 리스트 첫 번째 요소를 추출한다. 큐의 연산이다. 이 경우 전체복사가 필요하므로 O(n)이다.
# del a[i] # 시간 복잡도 : O(n) - 인덱스 i 의 요소를 삭제한다.
# a.sort() # 시간 복잡도 : O(n log n) - 정렬한다. 팀소트(Timsort)를 사용하며, 최선의 경우 O(n)에도 실행될 수 있다.
# min(a), max(a) # 시간 복잡도 : O(n) - 최솟값/최댓값을 계산한다.
# a.reverse() # 시간 복잡도 : O(n) - 뒤집는다. 리스트는 입력 순서가 유지되므로 뒤집게 되면 입력 순서가 반대로 된다.

# # dictionary
# words = ['apple', 'bat', 'bar', 'atom', 'book']
# by_letters = {}
#
# for word in words:
#     letter = word[0]
#     if letter not in by_letters:
#         by_letters[letter] = [word]
#     else:
#         by_letters[letter].append(word)
#
# print(by_letters)
# # {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}
# print(by_letters['c'])
# # KeyError: 'c'


# from collections import defaultdict
# words = ['apple', 'bat', 'bar', 'atom', 'book']
# by_letters = defaultdict(list)
# for word in words:
#     by_letters[word[0]].append(word)
# print(by_letters)
# # defaultdict(<class 'list'>, {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']})
# print(by_letters['c'])
# # []

# # 알고리즘 시작
# # Valid Palindrome
# #
# # Input: s = "A man, a plan, a canal: Panama"
# # Input: s = " "
# # Input: s = "race a car"
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True


# sol = Solution()
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
# print(sol.isPalindrome(" "))
# print(sol.isPalindrome("race a car"))
#
# import re
#
#
# class Solution2:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s = re.sub('[^a-z0-9]', '', s)
#         return s == s[::-1]
#
#
# sol = Solution2()
# print(sol.isPalindrome("A man, a plan, a canal: Panama"))
# print(sol.isPalindrome(" "))
# print(sol.isPalindrome("race a car"))
#
#
# # class Solution3:
# #     def isPalindrome(self, s: str) -> bool:
# #
#
#
# class Solution4:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s) - 1
#         while i < j:
#             a, b = s[i].lower(), s[j].lower()
#             if a.isalnum() and b.isalnum():
#                 if a != b:
#                     return False
#                 else:
#                     i, j = i + 1, j - 1
#                     continue
#             i, j = i + (not a.isalnum()), j - (not b.isalnum())
#         return True
#
#
# class Solution5:
#     def isPalindrome(self, s: str) -> bool:
#         # i starts at beginning of s and j starts at the end
#         i, j = 0, len(s) - 1
#         # While i is still before j
#         while i < j:
#             # If i is not an alpha-numeric character then advance i
#             if not s[i].isalnum():
#                 i += 1
#             # If j is not an alpha-numeric character then advance i
#             elif not s[j].isalnum():
#                 j -= 1
#             # Both i and j are alpha-numeric characters at this point so if they do not match return the fact that input was non-palendromic
#             elif s[i].lower() != s[j].lower():
#                 return False
#             # Otherwise characters matched and we should look at the next pair of characters
#             else:
#                 i, j = i + 1, j - 1
#         # The entire stirng was verified and we return the fact that the input string was palendromic
#         return True
#


# Reverse String
# Input: s = ["h","e","l","l","o"]
# Input: s = ["H","a","n","n","a","h"]
# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         """
#         Do not return anything, modify s in-place instead.
#         """
#
#
# class Solution2:
#     def reverseString(self, s: List[str]) -> None:
#         s[:] = reversed(s)
#         """
#         Do not return anything, modify s in-place instead.
#         """
#
#
# # Reorder Data in Log Files
# # Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# # Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         letter_logs = []
#         digit_logs = []
#
#         for log in logs:
#             if log.split()[1].isdigit():
#                 digit_logs.append(log)
#             else:
#                 letter_logs.append(log)
#
#         print(digit_logs)
#         print(letter_logs)
#
#         letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#         return letter_logs + digit_logs


# class Solution2:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         digits = []
#         letters = []
#         for log in logs:
#             if log.split()[1].isdigit():
#                 digits.append(log)
#             else:
#                 letters.append(log)
#         letters.sort(key=custom_sort)
#         return letters + digits
#
#
# def custom_sort(log: str) -> Tuple[str]:
#     identifier, content = log.split(" ", 1)
#     return content, identifier


# # Most Common Word
# # Input: paragraph = "a.", banned = []
# # Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# import re
# import collections
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
#         counts = collections.Counter(words)
#         return counts.most_common(1)[0][0]


# #
# import re

# class Solution2:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         # convert to lower case and split string into words by spaces and punctuation
#         a = re.split(r'\W+', paragraph.lower())
#
#         # make new list consisitng of words not in banned list (remove banned words)
#         b = [w for w in a if w not in banned]
#
#         # return value that counted max times in the new list
#         return max(b, key=b.count)

# class Solution3:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         my_dict = defaultdict(int)
#         # split string into list ignoring cases and punctuation
#         par = re.split("[" + string.punctuation + " " + "]+", paragraph.lower())
#         # keep counts of words in dict and keep track of most frequent
#         max_count = 0
#         max_word = ""
#         for word in par:
#             if word not in banned:
#                 my_dict[word] += 1
#                 if my_dict[word] > max_count:
#                     max_count = my_dict[word]
#                     max_word = word
#         return max_word

# from collections import Counter
# import re
#
#
# class Solution4:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         c = Counter(re.split('[!?\',;. ]', paragraph.lower()))
#         for (word, count) in c.most_common():
#             if word not in banned and word != '':
#                 return word
#
#
# import re
# import collections
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = re.findall(r'\w+', paragraph.lower())
#
#         counts = collections.defaultdict(int)
#         for word in words:
#             if word not in banned:
#                 counts[word] += 1
#
#         return max(counts, key=counts.get)
#
#
# Group Anagrams
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Input: strs = [""]
# Input: strs = ["a"]
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = {}
#         for word in strs:
#             sorted_word = "".join(sorted(word))
#             print(sorted_word)
#             # aet
#             # aet
#             # ant
#             # aet
#             # ant
#             # abt
#             if sorted_word in anagrams:
#                 anagrams[sorted_word].append(word)
#             else:
#                 anagrams[sorted_word] = [word]
#
#         return anagrams.values()
#     # [["eat","tea","ate"],["tan","nat"],["bat"]]

# #
# class Solution2:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         h = {}
#         for word in strs:
#             sortedWord = ''.join(sorted(word))
#             if sortedWord not in h:
#                 h[sortedWord] = [word]
#             else:
#                 h[sortedWord].append(word)
#         final = []
#         for value in h.values():
#             final.append(value)
#         return final
#
#
# class Solution3:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagrams = {}
#         for word in strs:
#             count = [0] * 26
#             for c in word:
#                 count[ord(c) - ord('a')] += 1
#             key = tuple(count)
#             if key in anagrams:
#                 anagrams[key].append(word)
#             else:
#                 anagrams[key] = [word]
#         return anagrams.values()
#
#
# class Solution4:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         strs_table = {}
#
#         for string in strs:
#             sorted_string = ''.join(sorted(string))
#
#             if sorted_string not in strs_table:
#                 strs_table[sorted_string] = []
#
#             strs_table[sorted_string].append(string)
#
#         return list(strs_table.values())


# # Timsort() 알고리즘
# def insertion_sort(arr, start, end):
#     for i in range(start + 1, end + 1):
#         key_item = arr[i]
#         j = i - 1
#         while j >= start and arr[j] > key_item:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key_item
#
#
# def merge(arr, start, mid, end):
#     if arr[mid - 1] <= arr[mid]:
#         return
#
#     left = arr[start:mid]
#     right = arr[mid:end]
#
#     k = start
#     i = 0
#     j - 0
#
#     while (start + i < mid and mid + j < end):
#         if(left[i] <= right[j]):
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1
#
#     if start + i < mid:
#         arr[k:end] = left[i:]
#     if mid + j < end:
#         arr[k:end] = right[j:]
#
#
# def timsort(arr):
#     min_run = 32
#     n = len(arr)
#
#     for i in range(0, n, min_run):
#         insertion_sort(arr, i, min((i + min_run - 1), n - 1))
#
#     size = min_run
#     while size < n:
#         for start in range(0, n, size * 2):
#             mid = start + size - 1
#             end = min((start + size * 2 - 1), (n - 1))
#             merge(arr, start, mid, end)
#         size += 2
#
#     return arr
#
#
# a = ['h', 'z', 's', 'y', 'b', 'c', 'd', 'e', 'f', 'g', ]
# print(timsort(a))


# # 스택 구현 - Last In First Out 방식
# #연결리스트의 노드를 표현할 클래스 정의
# class ListNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# #스택을 표현할 클래스 정의
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     #스택이 비어있는지 확인하는 메서드
#     def is_empty(self):
#         return self.size == 0
#
#     #스택의 맨 위에 원소를 추가하는 메서드
#     def push(self, value):
#         new_node = ListNode(value)
#         new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#
#     #스택의 맨 위에서 원소를 꺼내는 메서드
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("pop from an empty stack")
#         value = self.head.value
#         self.head = self.head.next
#         self.size -= 1
#         return value
#
# stack = Stack()
#
# #스택에 원소추가
# stack.push(1)
# stack.push(3)
# stack.push(2)
# stack.push(4)
# stack.push(5)
#
#
# for _ in range(5):
#     print(stack.pop()) #스택에서 원소 꺼냄
#
#
# # Valid Parentheses (괄호로 된 입력값이 올바른지 판별)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {
#             ')': '(',
#             '}': '{',
#             ']': '['
#         }
#
#         for char in s:
#             # 스택 마지막 요소 꺼내서 확인, 비어있으면 #반환
#             if char in mapping:
#                 top_element = stack.pop() if stack else '#'
#
#             else:
#                 stack.append(char)
#
#         return not stack
#
# # Remove Duplicate Letters (중복 문자 제거)
# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         if not s:
#             return ""
#
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ""))
#                 return ""
#
# # 2
# class Solution2:
#     def removeDuplicateLetters(self, s: str) -> str:
#         if not s:
#             return ""
#
#         #문자열의 문자 빈도수 계산
#         counter = {char: 0 for char in set(s)}
#         for char in s:
#              counter[char] += 1
#
#         # 사전순으로 가장 작은 문자의 인덱스 찾기
#         min_idx = 0
#         for i, char in enumerate(s):
#             if char < s[min_idx]:
#                 min_idx = i
#             counter[char] -= 1
#             if counter[char] == 0:
#                 break
#         return s[min_idx] + self.removeDuplicateLetters(s[min_idx + 1:].replace(s[min_idx], ""))
#
# # 3
# class Solution3:
#     def removeDuplicateLetters(self, s: str) -> str:
#         last_occurrence = {c: i for i, c in enumerate(s)}
#         stack = []
#         in_stack = set()
#
#         for i, c in enumerate(s):
#             if c not in in_stack:
#                 while stack and c < stack[-i] and i < last_occurrence[stack[-1]]:
#                     in_stack.remove(stack.pop())
#                 stack.append(c)
#                 in_stack.add(c)
#
#         return ''.join()
#
#
# # Daily Temperatures (일일 온도)
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         answer = [0] * len(temperatures)
#         stack = []
#
#         for i, cur in enumerate(temperatures):
#             while stack and cur > temperatures[stack[-1]]:
#                 last = stack.pop()
#                 answer[last] = i - last
#             stack.append(i)
#
#         return answer

# import requests
#
# print(requests)

# Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         front_pointer = head
#         back_pointer = head
#
#         while front_pointer is not None and front_pointer.next is not None:
#             back_pointer = back_pointer.next
#             front_pointer = front_pointer.next.next
#
#             if back_pointer == front_pointer:
#                 return 1
#         return 0
#
#
# class Solution2:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         # 집합의 중복은 재거하는 특성을 이용한 풀이방법
#         node_seen = set()
#
#         # head 가 나올 때 까지 계속 돌면서
#         while head is not None:
#             # head 가 등장 하면
#             if head in node_seen:
#                 return True
#
#             # 계속 추가해주고
#             node_seen.add(head)
#             head = head.next
#         return False
#
# class Solution3:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         if not head or not head.next:
#             return False
#
#         slow = head
#         fast = head.next
#
#         while slow != fast:
#             if not fast or not fast.next:
#                 return False
#             slow = slow.next
#             fast = fast.next.next
#
#         return True


# # 그래프 알고리즘
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# visited = set() # 방문한 노드를 저장할 집합
#
# # DFS (깊이 우선 탐색) - 재귀 함수
# def dfs_recursive(node):
#     if node not in visited:
#         print(node, end=' ')
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs_recursive(neighbor)
#
# # 시작 노드 설정 및 함수 호출
# start_node = 'A'
# dfs_recursive(start_node)
#
# # DFS (깊이 우선 탐색) - 스택 사용
# def dfs_iterative(start_node):
#     stack = [start_node]
#
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
#
# # 시작 노드 설정 및 함수 호출
# start_node = 'A'
# dfs_iterative(start_node)
#
# # BFS (너비 우선 탐색) - 큐를 이용한 반복 구조로 구현
# from collections import deque
# def bfs_iterative(start_node):
#     queue = deque([start_node]) # BFS 큐 초기화
#
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             queue.extend(graph[node])
#
# # 시작 노드 설정 및 함수 호출
# start_node = 'A'
# bfs_iterative(start_node)


# # BFS : 강사님 코드
# from collections import deque
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# visited = set()
# def bfs_iterative(start_node):
#     queue = deque([start_node])
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             queue.extend(graph[node])
# def dfs_iterative(start_node):
#     stack = [start_node]
#
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=' ')
#             visited.add(node)
#             stack.extend(reversed(graph[node]))
#
# snode = 'A'
# dfs_iterative(snode)
# visited.clear()
# print('\n-----')
# bfs_iterative(snode)

# # 20230620
# # Leetcode
# # Letter Combinations of a Phone Number : DFS??
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#
#         phone = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }
#
#         def backtrack(combination, next_digits):
#             if len(next_digits) == 0:
#                 output.append(combination)
#
#             else:
#                 for letter in phone[next_digits[0]]:
#                     backtrack(combination + letter, next_digits[1:])
#
#         output = []
#         backtrack("", digits)
#         return output
#
#
# # 강사님 코드
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         def dfs(index, path):
#             if len(path) == len(digits):
#                 result.append(path)
#                 return
#             for i in range(index, len(digits)):
#                 for j in dic[digits[i]]:
#                     dfs(i + 1, path + j)
#
#         if not digits:
#             return []
#
#         dic = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }
#
#         result = []
#         dfs(0, "")
#
#         return result
#
#
# # Permutations
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         # 결과를 저장할 리스트
#         result = []
#
#         # 주어진 리스트의 순열을 찾는 함수
#         def find_permutations(nums, current_permutation):
#             # 만약 주어진 리스트가 비었다면, 현재의 순열을 결과에 추가
#             if not nums:
#                 result.append(current_permutation)
#                 return
#
#             # 주어진 리스트의 모든 숫자에 대해 순열 찾기
#             for i in range(len(nums)):
#                 # 숫자를 선택하고, 선택하지 않은 숫자들에 대해 순열 찾기
#                 remaining_nums = nums[:i] + nums[i + 1:]
#                 new_permutation = current_permutation + [nums[i]]
#                 find_permutations(remaining_nums, new_permutation)
#
#         # 주어진 숫자들에 대해 순열 찾기 시작
#         find_permutations(nums, [])
#
#         # 결과 반환
#         return result
#
#
# # 강사님 코드
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(path):
#             if len(path) == len(nums):
#                 result.append(path[:])
#                 return
#
#             for i in range(len(nums)):
#                 if nums[i] in path:
#                     continue
#                 dfs(path + [nums[i]])
#
#         result = []
#         dfs([])
#         return result
#
#
# # Reconstruct Itinerary
# from collections import defaultdict
#
#
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         # 그래프를 만들어. 공항을 키로하고 출발과 도착을 값으로 가지는 딕셔너리로
#         # 도착지들은 우선순위 큐로 관리 (lexical)
#         graph = defaultdict(list)
#
#         # reverse 를 써서 뒤집어 두면 나중에 pop()으로 해결 가능
#         for depart, arrive in sorted(tickets, reverse=True):
#             graph[depart].append(arrive)
#
#         route = []
#
#         def dfs(airport):
#             while graph[airport]:
#                 dfs(graph[airport].pop())
#             route.append(airport)
#
#         dfs("JFK")
#         return route[::-1]
#
#
# # 강사님 코드
# from collections import defaultdict
#
#
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)
#
#         route = []
#
#         def visit(city):
#             while graph[city]:
#                 next_city = graph[city].pop(0)
#                 visit(next_city)
#             route.append(city)
#
#         visit("JFK")
#         return route[::-1]
#
#
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         graph = collections.defaultdict(list)
#         for a, b in sorted(tickets):
#             graph[a].append(b)
#
#         route = []
#         stack = ["JFK"]
#
#         while stack:
#             while graph[stack[-1]]:
#                 stack.append(graph[stack[-1]].pop(0))
#             route.append(stack.pop())
#
#         return route[::-1]
#
#
# # Network Delay Time : 다익스트라 알고리즘
# import collections
# import heapq
#
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         # 그래프 구성
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v, w))
#
#         # 큐 변수: [(소요 시간, 정점)]
#         Q = [(0, k)]
#         dist = collections.defaultdict(int)
#
#         # 우선순위 큐 최소값 기준으로 정점까지 최단 경로 삽입
#         while Q:
#             time, node = heapq.heappop(Q)
#             if node not in dist:
#                 dist[node] = time
#                 for v, w in graph[node]:
#                     alt = time + w
#                     heapq.heappush(Q, (alt, v))
#
#         # 모든 노드의 최단 경로 존재 여부 판별
#         if len(dist) == n:
#             return max(dist.values())
#         return -1
#
#
# # 강사님 코드
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v, w))
#
#         Q = [(0, k)]
#         dist = collections.defaultdict(int)
#
#         while Q:
#             time, node = heapq.heappop(Q)
#             if node not in dist:
#                 dist[node] = time
#                 for v, w in graph[node]:
#                     alt = time + w
#                     heapq.heappush(Q, (alt, v))
#
#         # 모든 노드의 최단 경로 존재 여부 판별
#         if len(dist) == n:
#             return max(dist.values())
#         return -1


# 20230621 : 오전 알고리즘 수업
# leetcode : Maximum Depth of Binary Tree - 트리

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 가장 먼저 입력값이 없으면 (항상 예외 처리를 먼저 신경쓰자)
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


# 강사님 코드
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                current_root = queue.popleft()
                if current_root.left:
                    queue.append(current_root.left)
                if current_root.right:
                    queue.append(current_root.right)
        return depth


# leetcode : Longest Univalue Path
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node:
                return 0

            left_length = arrow_length((node.left))
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0

            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1

            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1

            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


# 강사님 코드
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(node):
            if not node:
                return 0

            left_length = dfs(node.left)
            right_length = dfs(node.right)

            left_arrow = right_arrow = 0

            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1

            self.longest_path = max(self.longest_path, left_arrow + right_arrow)

            return max(left_arrow, right_arrow)

        dfs(root)
        return self.longest_path


# leetcode : Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None:
                return 0

            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1

            return max(left, right) + 1

        return check(root) != -1

# 강사님 코드
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node):
            if not node:
                return 0

            left_height = check_height(node.left)
            right_height = check_height(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            return max(left_height, right_height) + 1

        return check_height(root) != -1


# leetcode : Minimum Height Trees
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = collections.defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


# leetcode : Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            if low <= node.val <= high:
                self.total += node.val

            if low < node.val:
                dfs(node.left)

            if node.val < high:
                dfs(node.right)

        self.total = 0
        dfs(root)
        return self.total


# 강사님 코드
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0

        # node 트리 탐색 하겠다!
        def dfs(node):
            if not node:
                return 0

            if low <= node.val <= high:
                self.answer += node.val

            if low < node.val:
                dfs(node.left)
            if high > node.val:
                dfs(node.right)

        dfs(root)
        return self.answer