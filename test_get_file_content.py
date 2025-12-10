from functions.get_file_content import get_file_content

print("Content length of lorem.txt:")
result = get_file_content("calculator", "lorem.txt")
if result.startswith("Error:"):
    print(result)
else:
    print(len(result))
    print(result.endswith('[...File "lorem.txt" truncated at 10000 characters]'))

print("Content length of main.py:")
result = get_file_content("calculator", "main.py")
if result.startswith("Error:"):
    print(result)
else:
    print(result)

print("Content length of pkg/calculator.py:")
result = get_file_content("calculator", "pkg/calculator.py")
if result.startswith("Error:"):
    print(result)
else:
    print(result)

print("Content length of /bin/cat:")
result = get_file_content("calculator", "/bin/cat")
if result.startswith("Error:"):
    print(result)
else:
    print(len(result))

print("Content length of pkg/does_not_exist.py:")
result = get_file_content("calculator", "pkg/does_not_exist.py")
if result.startswith("Error:"):
    print(result)
else:
    print(len(result))
