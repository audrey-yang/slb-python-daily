"""
Show me the Clock

Difficulty: Hard
Question: Write a program that prints the sand clock pattern.
"""

def gen_sand_clock(n: int) -> None:
    """
    Print a sand clock pattern of size n (height n * 2)

    Args:
        n: The size of the pattern. Must be greater than 2.
    """
    assert n > 2

    print("* " * n, "*", sep="")
    for i in range(1, n):
        space_outer, space_inner = i, (2 * n) - (2 * i) - 1
        print(" " * space_outer, "*", " " * space_inner, "*", " " * space_outer, sep="")
    for i in range(n - 1, 0, -1):
        space_outer, space_inner = i, (2 * n) - (2 * i) - 1
        print(" " * space_outer, "*", " " * space_inner, "*", " " * space_outer, sep="")
    print("* " * n, "*", sep="")

if __name__ == "__main__":
    print("SAND CLOCK, SIZE 3")
    gen_sand_clock(3)

    print("\nSAND CLOCK, SIZE 9")
    gen_sand_clock(9)
