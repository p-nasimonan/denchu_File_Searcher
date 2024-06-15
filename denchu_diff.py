
import glob
import os

path1 = 'seventh/denchu2024/'
path2 = 'eighth/denchu2024/'
path3 = 'ninth/denchu2024/'

def SarchPath(path:str) -> tuple[list[str], list[str]]:
    path = os.getcwd()+'/'+path
    result = glob.glob(path+'**', recursive=True)
    relative_result = [result[i].replace(path,'') for i in range(len(result))]
    return result, relative_result

def ConpareList(list1, list2) -> tuple[dict[int,str], dict[int,str]]:
    '''

    {含む場所(含まないなら含まれてた番号のマイナス):内容}
    difw12 list1の要素はlist2に含まれるのか 
    difw21 list2の要素はlist1に含まれるのか

    例
    >>> lis1 = ['a', 'b', 'c']
    >>> lis2 = ['a', 'c', 'd']
    >>> print(ConpareList(lis1, lis2))
    (False, {0: 'a', -1: 'b', 1: 'c'}, {0: 'a', 2: 'c', -1: 'd'})
    '''

    difw12:dict = {}
    difw21:dict = {}
    for i in list1:
        try:
            difw12[list2.index(i)] = i
        except ValueError:
            difw12[-1 * list1.index(i)] = i

    for i in list2:
        try:
            difw21[list1.index(i)] = i
        except ValueError:
            difw21[-1 * list2.index(i)] = i

    return difw12, difw21

#あとはファイルの中身を比較したい
def AllFileInport(file:dict, ls:list, rela_ls:list):
        for path, rela_path in zip(ls, rela_ls):
            try:
                with open(path, 'r', encoding="utf-8") as f:
                        file[rela_path] = f.read()
            except:
                pass
        return file

def ConpareFile(file1:dict, file2:dict):
    def Conpareter(files1:dict, files2:dict, path1:list, path2:list):
        paths = set(set(path1) & set(path2))
        difF12:dict = {}
        difF21:dict = {}
        word1:dict = {}
        word2:dict = {}
        for path in paths:
            file1 = files1[path]
            file2 = files2[path]
            if not file1==file2:
                word1[path] = file1.split('\n')
                word2[path] = file2.split('\n')
                difF12[path], difF21[path] = ConpareList(word1[path], word2[path])
        return difF12, difF21, paths

    path1, path2 = list(file1), list(file2)
    result = Conpareter(file1, file2, path1, path2)
    del file1, file2, path1, path2
    return result
    

def NoneIncludeElement(data:dict, recursive=False):
    if recursive:
        for key in data:
                print('-----'+key+'------')
                return NoneIncludeElement(data[key])
    else:
        list = [data[k] for k in data if k < 0]
        for k in data:
            if k < 0:
                print(data[k])
        return list
def IncludeElement(data:dict[int, str]):
    list = [data[k] for k in data if k >= 0]
    return list

ls1, rela_ls1 = SarchPath(path1)
ls2, rela_ls2 = SarchPath(path2)
ls3, rela_ls3 = SarchPath(path3)

FILE1:dict = {}
FILE2:dict = {}
FILE3:dict = {}
FILE1 = AllFileInport(FILE1, ls1, rela_ls1)
FILE2 = AllFileInport(FILE2, ls2, rela_ls2)
FILE3 = AllFileInport(FILE3, ls3, rela_ls3)


difP12, difP21 = ConpareList(rela_ls1, rela_ls2)
difP23, difP32 = ConpareList(rela_ls2, rela_ls3)

difF12, difF21, paths12 = ConpareFile(FILE1, FILE2)
difF23, difF32, paths23 = ConpareFile(FILE2, FILE3)


print('====セブンとエイト=========\n===========================\n [-]')
NoneIncludeElement(difP12)
print('#####################')
NoneIncludeElement(difF12, recursive=True)
print('=================\n [+]')
NoneIncludeElement(difP21)
print('////Replace File\\\\\\\\')
NoneIncludeElement(difF21, recursive=True)
print('=====エイトとナイン========\n===========================\n [-]')
NoneIncludeElement(difP23)
print('////Replace File\\\\\\\\')
NoneIncludeElement(difF23, recursive=True)
print('=================\n [+]')
NoneIncludeElement(difP32)
print('////Replace File\\\\\\\\')
NoneIncludeElement(difF32, recursive=True)