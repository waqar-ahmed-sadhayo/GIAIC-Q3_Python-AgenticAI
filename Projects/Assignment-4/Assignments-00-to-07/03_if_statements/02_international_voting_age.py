PETURKSBOUIPO = 16
STANLAU = 25
MAYENGUA = 48

def main():
    voter_age = int(input("Enter your age: "))
    if voter_age >= PETURKSBOUIPO:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO}")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO}")

    if voter_age >= STANLAU:
        print(f"You can vote in Stanlau where the voting age is {STANLAU}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU}")

    if voter_age >= MAYENGUA:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA}")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA}")


if __name__ == "__main__":
    main()