import re

def getData(fileName):
    f = open(fileName, "r")
    content = f.read()
    trucks = re.search("trucks: (\d+)", content, re.MULTILINE)
    print(trucks)
    optimalValue = re.search("Optimal value: (\d+)", content, re.MULTILINE)
    if(optimalValue != None):
        optimalValue = optimalValue.group(1)
    else:
        optimalValue = re.search("Best value: (\d+)", content, re.MULTILINE)
        if(optimalValue != None):
            optimalValue = optimalValue.group(1)
    capacity = re.search("^CAPACITY : (\d+)$", content, re.MULTILINE).group(1)
    graph = re.findall(r"^(\d+) (\d+) (\d+)$", content, re.MULTILINE)
    demand = re.findall(r"^(\d+) (\d+)$", content, re.MULTILINE)
    graph = {int(a):(int(b),int(c)) for a,b,c in graph}
    demand = {int(a):int(b) for a,b in demand}
    capacity = int(capacity)
    trucks = trucks.group(1)
    trucks=int(trucks)
    print(trucks)
    optimalValue = int(optimalValue)
    return capacity, graph, demand, optimalValue, trucks