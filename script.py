import sys

args = sys.argv

buffer = []

for i in range(1, len(args)-1):
    f = open("{}".format(args[i]), 'r')
    lines = f.read().splitlines()
    buffer.extend(lines)

buffer = set(buffer)
buffer = list(buffer)

with open("{}".format(args[-1]), "w") as outfile:
    outfile.write("\n".join(buffer))
