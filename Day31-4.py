#ファイル入力
# file_path = 'resources/input.csv'
# f = open(file_path, mode='r',encoding='utf-8')
#
# # line = f.read() #中身全体
# # print(line)
#
# # lines = f.readlines()
# # print(lines)
# # for i in lines:
# #     print(i.rsplit('\n'))
#
# line = f.readline()
# while line:
#     print(line.rstrip('\n'))
#     line = f.readline()
#
# f.close() #ファイルを閉じる -> メモリを食う、他の処理をファイルが開けなくなる可能性がある。
#
# # with
# with open(file_path, mode='r',encoding='utf-8') as f:
#     lines = f.readlines()
#     print(lines)
#
# print(f.read())


#ファイル出力, 追記

file_path = 'resources/output.csv'
f = open(file_path, mode='w',encoding='utf-8', newline='\n')
f.write('あああああ\nいいいいい')
f.close()

with open(file_path, mode='a', encoding='utf-8', newline='\n') as f:
    list_a = [
        ['A', 'B', 'C'],
        ['あ','い','う']
    ]
    for x in list_a:
        f.write('\n')
        f.write(','.join(x))

    # f.writelines(list_a[0])
