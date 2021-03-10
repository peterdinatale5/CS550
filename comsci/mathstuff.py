import math
import sys

x = float(sys.argv[1])

result = math.sin((10*math.pi)/x)

result2 = (math.sin(math.pi*x) * 2) + (math.cos(math.pi*x) * 3)

print(result)
