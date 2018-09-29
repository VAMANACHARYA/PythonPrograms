'''File reading '''
InputFile = open("Input.txt", "r")
lines = InputFile.readlines()

'''Create a list to store reveresed results'''
results = []
OutPutFile = open("Output.txt","w")
def reverse (text):
    lenth = len(text)
    for i in range(lenth, -1, -1):
        results.append(text[i-1])

for i in range(len(lines)):
    reverse(lines[i])

for item in range(len(results)):
    (OutPutFile.write(results[item]))

OutPutFile.close()
InputFile.close()
