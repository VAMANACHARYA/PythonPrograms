InputFile = open("Input.txt", "r")

lines = InputFile.readlines()
results = []

OutPutFile = open("Output.txt","w")
def reverse (text):
    lenth = len(text)
    for i in range(lenth, 0, -1):
        print text[i-1],
        results.append(text[i-1])



for i in range(len(lines)):
    reverse (lines[i])
    print('\n')

for item in range(len(results)):
    print results[item],
    OutPutFile.write(results[item])

print ('\n')

print type(results)

InputFile.close()
OutPutFile.close()
