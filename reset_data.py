import os

def reset():
    arq = open(os.path.join("assets", "pontos.txt"), "w")
    for i in range(100):
        k = str(i*10) + " " + str(i) + "\n"
        arq.write(k)
    arq.close()
reset()
