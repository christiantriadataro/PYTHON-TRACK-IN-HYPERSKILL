# 10 files
# Create 10 files, file1.txt, file2.txt and so on till
# fill10.txt. The files should contain the number
# corresponding to their name. So, file1.txt should
# contain one line with number 1, file2.txt - one line
# with number 2 and so on.

for i in range(1, 11):
    with open(f"file{i}.txt", 'w') as f:
        f.write(f"{i}")
        