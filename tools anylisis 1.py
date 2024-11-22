def title(word):
    print()
    print(f"------ {word} ------")
    print()

def Tools_Analysis_OC(text):
    title("Lengths")

    print(f"Length : {len(text)}")
    countL = 0
    for x in text:
        if x == " ":
            countL +=1
    print(f"Cipher Characters : {len(text)-countL}")


    title("Freqs.")
    store = []
    upperText = text.upper()
    for x in range(26):
        let = 65 + x
        count = 0
        for y in upperText:
            if y == chr(let):
                count +=1
        store.append(count)
        
    for counter in range(26):
        let = 65 + counter
        print(f"{chr(let)} : {store[counter]}")
        



Tools_Analysis_OC("hello my name is bob")
