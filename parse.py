def rep(x):
    x.replace("Lat: ", "|")
    x.replace("Long: ", "|")
    x.replace("Alt: ", "|")
    x.replace("Radial Accuracy: ", "|")
    x.replace("Speed:", "|")
logFileName = input("File Name: ")
with open(logFileName, 'r') as f:
    logData = f.readlines()
logData = [x.replace(" ","") for x in logData]
logData = [x.replace("Time:", "") for x in logData]
logData = [x.replace("Lat:", "|") for x in logData]
logData = [x.replace("Long:", "|") for x in logData]
logData = [x.replace("Alt:", "|") for x in logData]
logData = [x.replace("RadialAccuracy:", "|") for x in logData]
logData = [x.replace("Speed::", "|") for x in logData]
F = open(logFileName + " Output.txt", "w")
F.write("Number|Time|Lat|Long|Alt|Radial Accuracy|Speed\n")
for line in logData:
    F.write(line)
F.close()

