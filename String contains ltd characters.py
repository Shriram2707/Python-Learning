#Assignment 2: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.
#Example 1:
#Input: s = "()" Output: true Example 2:
#Input: s = "()[]{}" Output: true Example 3:
#Input: s = "(]" Output: false Example 4:
#Input: s = "([)]" Output: false Example 5:
#Input: s = "{[]}" Output: true
#Constraints:
#1 <= s.length <= 104 s consists of parentheses only '()[]{}'.
#Method 1
s = input("Enter string with () {} or []: ")
if s.startswith("(") and s.endswith(")"):
    print(s, "Is Valid String")
elif s.startswith("[") and s.endswith("]"):
    print(s, "Is Valid String")
elif s.startswith("{") and s.endswith("}"):
    print(s, "Is Valid String")
else:
    print(s, "Is Not Valid String")

#Method 2:
s = input("Enter string with () {} or []: ")
if s.startswith("(" or "{" or "[") and s.endswith(")" or "}" or "]"):
    print(s, "Is Valid String")
else:
    print(s, "Is Not Valid String")
