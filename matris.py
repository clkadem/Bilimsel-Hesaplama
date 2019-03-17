denklem = [[1,2,1],[3,4,2]]
def denklemcoz(matris):
    b = 0
    for i in range(len(matris)-1,-1,-1):
        d=(-matris[i][b]/matris[b][b])
        for j in range(0,len(matris[i])):
            matris[i][j] = d*matris[b][j] + matris[i][j]
        b=b+1
    b=0
    for k in range(0,len(matris)):
        c=matris[k][b]
        for z in range(0,len(matris[k])):
            matris[k][z]=matris[k][z]/c
        b=b+1

    return matris

print(denklemcoz(denklem))
print("x : ",denklem[0][2]/denklem[0][0],"  y : ",denklem[1][2]/denklem[1][1])