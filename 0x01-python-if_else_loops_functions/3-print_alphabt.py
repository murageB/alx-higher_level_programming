#!/usr/bin/python3
for alpha in range(97, 122):
      if alpha == ord('e') or alpha == ord('q'):
         continue
      print("{:c}".format(alpha), end="")
