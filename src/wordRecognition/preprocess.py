
f = open("/Users/Ivan/nGram_1-5_ge2times.txt", "w")
for line in open("/Users/Ivan/nGram_1-5_all.txt"):
    if int(line.split('|')[1]) > 1:
        f.write(line)
f.close()
