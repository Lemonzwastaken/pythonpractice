with open(r"mail-merger\Input\Names\invited_names.txt") as file:
    names = file.readlines()
    names_stripped = []
    for name in names:
        names_stripped.append(name.strip("\n"))


with open(r"mail-merger\Input\Letters\starting_letter.txt") as file:
    letter = file.read()

for name in names_stripped:
    with open(f"mail-merger\Output\Letters\letter-to-{name}.txt", "w") as file:
        changed_letter = letter.replace("[name]", name)
        file.write(changed_letter)