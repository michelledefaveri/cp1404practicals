"""
Estimated time: 20 minutes
Actual time: 16 minutes
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Put the language objects into a list
languages = [python, ruby, visual_basic]

print(python)

# Display only the languages that use dynamic typing
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
