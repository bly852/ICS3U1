fieldSize = int(input("enter size :"))
text = input("enter text :")

textL = len(text)

numas = fieldSize-(textL+2)
leftS = numas//2
rightS = numas-leftS

topS = (fieldSize-3)//2
bottomS = (fieldSize-3)-topS

print(("\n" + "X"*fieldSize)*topS)
print("X"*leftS," "*textL, "X"*rightS)
print("X"*leftS, text, "X"*rightS)
print("X"*leftS," "*textL, "X"*rightS)
print(("X"*fieldSize + "\n")*bottomS)