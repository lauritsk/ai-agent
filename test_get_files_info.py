from functions.get_files_info import get_files_info

print("Result for current directory:")
results = get_files_info("calculator", ".").split("\n")
for result in results:
    print(f"  {result}")

print("Result for 'pkg' directory:")
results = get_files_info("calculator", "pkg").split("\n")
for result in results:
    print(f"  {result}")

print("Result for '/bin' directory:")
results = get_files_info("calculator", "/bin").split("\n")
for result in results:
    print(f"  {result}")

print("Result for '../' directory:")
results = get_files_info("calculator", "../").split("\n")
for result in results:
    print(f"  {result}")
