input_list=list(map(int,input().split()))
for i in range(len(input_list)):
    stage=input_list[i]
    trangle=[[1]*ii for ii in range(1,stage+1)]
    for row in range(stage):
        for col in range(1,row):
            trangle[row][col]=trangle[row-1][col]+trangle[row-1][col-1]
    for row in range(stage):
        for col in range(row):
            print(trangle[row][col],end=' ')
        print(trangle[row][-1])
    print()