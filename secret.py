def secret_code(message, coding):
    words = message.split(" ")
    if coding:
        nwords = []
        for word in words:
            if len(word) >= 3:
                prefix = "gsw"
                suffix = "hbk"
                stnew = prefix + word[1:] + word[0] + suffix
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
        print("Encoding is done")
    else:
        nwords = []
        for word in words:
            if len(word) >= 3 and word.startswith("gsw") and word.endswith("hbk"):
                stnew = word[3:-3]
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print(" ".join(nwords))
        print("Decoding is done")

# Input from the user
message = input("Enter the message: ")
coding_input = input("Enter 1 for coding or 0 for decoding: ")

# Convert coding_input to a boolean value
coding = True if coding_input == "1" else False

# Call the function
secret_code(message, coding)
