import sys

number=int (sys.argv[1])

for i in range(1,101):
  if 100%number==0:
    print(i,end="")

print()
