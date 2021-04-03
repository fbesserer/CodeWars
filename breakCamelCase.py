# Complete the solution so that the function will break up camel casing, using a space between words.
# example: solution("camelCasing")  ==  "camel Casing"
import test

def solution(s):
    sub_strings = []
    mark = 0
    for pos, char in enumerate(s):
        if char.isupper():
            sub_strings.append(s[mark:pos] + " ")
            mark = pos
    sub_strings.append(s[mark:])
    return "".join(sub_strings)


def solution(s):
    return ''.join(" " + c if c.isupper() else c for c in s)


print("Pass" if solution("helloWorld") == "hello World" else "Fail")
print("Pass" if solution("camelCase") == "camel Case" else "Fail")
print("Pass" if solution("breakCamelCase") == "break Camel Case" else "Fail")