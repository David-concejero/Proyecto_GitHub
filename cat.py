import sys

if len(sys.argv) != 2:
  sys.stderr.write('to run with one arguments\n')
  exit()
try:
  fh = open(sys.argv[1],"r")
except FileNotFoundError:
  sys.stderr.write(sys.argv[1] + ' not exists \n')
  exit()
fe = open("upper","w")
line = fh.readline().strip()
while line:
  if line.isupper():
   fe.write(line + '\n')
  if line.isnumeric():
   print("Número: " + str(line))
  line = fh.readline().strip()
fh.close()
fe.close()

# Esto es una modificación realizada para el examen del dia 28/11/2018
