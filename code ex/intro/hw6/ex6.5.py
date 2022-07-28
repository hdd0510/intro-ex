# cho 1 file gồm tên người, đồ vật mua, số lượng: Dũng giấy 10
#                                                 dinzdzun bcs 20
#                                                 Dũng áo mưa 10
#                                                 dinzdzun thuốc ngủ 5
def process(filepath):
    lst = []
    with open(filepath, 'r') as f:
        for i in f:
            a = i.split()
            #tạo list gồm các thông tin với cấu trúc: tên, [vật, số lượng]
            lst.append([a[0], [a[1], a[2]]])
    #tạo dict để gộp vật với tên
    res = {}
    for i in lst:
        if i[0] not in res:
            #nếu tên chưa xuất hiện thì thêm tên vào res đồng thời tạo cho tên 1 dict con
            res[i[0]] = {}
        if i[0] in res:
            #tên đã xuất hiện
            if i[1][0] not in res[i[0]]:
                #nếu vật chưa xuất hiện thì thêm vật là key và gán value
                res[i[0]][i[1][0]] = int(i[1][1])
            else:
                #nếu vật xuất hiện rồi thì + thêm value
                res[i[0]][i[1][0]] += int(i[1][1])
    a = list(sorted(res.items())) #sort theo tên
    res = dict(a)
    for i in res:
        a = list(sorted(res[i].items())) #sort theo đồ vật
        a.sort()
        res[i] = dict(a)
        print(i,":", sep="")
        for j in res[i]:
            print(j, res[i][j])
        


