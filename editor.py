result = []
help_message = """1.Ask a user to input a formatter.
2. If the formatter doesn't exist, print the following error message: Unknown formatting type or command. Please try again.
3. Ask a user to input a text that will be applied to the formatter: - Text: <user's input>.
4. Save the text with the chosen formatter applied to it and print the markdown."""

while True:
    x = input("- Choose a formatter: ")

    if x == "!done":
        try:

            file = open("output.md", "w")

            for item in result:
                file.write(item)

            file.close()

        except FileExistsError:

            print("Failed to save file.")

        break

    if x == "header":
        level = int(input("- Level: "))
        text = input("- Text: ")
        sig = "#"
        header = f'{sig * level} {text}\n'
        result.append(header)
        print(*result, sep="")
        continue

    elif x == "plain":
        some_plain = input("- Text: ")
        result.append(some_plain)
        print(*result, sep="")

    elif x == "new-line":
        result.append('\n')
        print(*result, sep="")

    elif x == "link":
        label = input("Label: ")
        url = input("URL: ")
        label_url = f"[{label}]({url})"
        result.append(label_url)
        print(*result, sep="")

    elif x == "bold":
        bold = input("Text: ")
        result.append(f"**{bold}**")
        print(*result, sep="")

    elif x == "italic":
        italic = input("Text: ")
        result.append(f"*{italic}*")
        print(*result, sep="")

    elif x == "inline-code":
        inline = input("Text: ")
        result.append(f"`{inline}`")
        print(*result, sep="")

    elif x == "unordered-list" or x == "ordered-list":
        rows = 0

        while rows < 1:
            rows = int(input("Number of rows: "))
            if rows < 1:
                print("The number of rows should be greater than zero")
        for i in range(1, rows + 1):
            row = input(f"Row #{i}: ")
            if x == "ordered-list":
                result.append(f"{i}. {row}\n")

            else:
                result.append(f"* {row}\n")

        print(*result, sep="")

    else:
        print("Unknown formatting type or command. Please try again.")
        continue
