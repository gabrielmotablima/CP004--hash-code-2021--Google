from pydash import *

f = open('b.txt')

L = []

read_lines = f.readlines()
for line in read_lines:
  L.append(str(line).replace('\n', '').split(' '))

f.close()


new_L = []
for i in range(int(L[0][1])):
  for line in L[1:]:
    if line[1] == str(i):
      new_L.append(line)
new_L

num_nodes = map_(new_L, lambda x: x[1])
nodes = []

for n in range(int(L[0][1])):
  nodes.append([n, num_nodes.count(str(n))])


ant = 0
tmp = 0
string_da_vitoria = str(L[0][1]) + "\n"


for i in range(len(nodes)):
  string_da_vitoria += str(nodes[i][0]) + "\n" + str(nodes[i][1]) + "\n"
  for line in new_L[ant:ant+nodes[i][1]]: 
    string_da_vitoria += line[2] + " 1\n"
  ant += nodes[i][1]

file_vitoria = open("b_submission.txt", "w")
file_vitoria.write(string_da_vitoria)
file_vitoria.close()