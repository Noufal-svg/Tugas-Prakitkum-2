def print_pattern(lines: int):
    for i in range(lines):
        print(
            "*"*(lines-i+1), "*","_*"*i,sep="",
        )
print_pattern(5)