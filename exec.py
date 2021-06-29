# 버그 리스트 프로그램
print("-- Bug List --")
print("-- <q:quit> --")
text = []
c = 0
while True:
    c += 1
    text = input(f"{c}. ")
    if text.find('q')==0:
        print("-> (QUIT) <-")
        break

