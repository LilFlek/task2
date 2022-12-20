data = input("Enter brackets: ")
word = input("Enter word: ")

whitelist = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}"
}

for k in data:
    if k not in whitelist.keys() and k not in whitelist.values():
        data = data.replace(k, '')
        print(k)

if not data:
    print("Invalid brackets format.")
elif len(data) % 2 != 0:
    print("Unclosed brackets are not supported.")
else:
    invalid = False

    for i in range(len(data) // 2):
        opposite = data[len(data) - i - 1]
        current = data[i]
        if opposite != whitelist[current]:
            print("Invalid order")
            invalid = True
            break

    if not invalid:
        print(data[:len(data) // 2] + word + data[len(data) // 2:])
