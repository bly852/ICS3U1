fieldSize = int(input("Enter number: "))
text = input("Enter text: ")

textL = len(text)

numas = fieldSize-(textL+2)
leftS = numas//2
rightS = numas-leftS

topS = (fieldSize-3)//2
bottomS = (fieldSize-3)-topS

print(("\n" + "*"*fieldSize)*topS)
print("*"*leftS," "*textL, "*"*rightS)
print("*"*leftS, text, "*"*rightS)
print("*"*leftS," "*textL, "*"*rightS)
print(("*"*fieldSize + "\n")*bottomS)