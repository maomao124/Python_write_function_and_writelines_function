"""
 * Project name(项目名称)：Python_write函数和writelines函数
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:16
 * Version(版本): 1.0
 * Description(描述)： writelines()函数
 """

if __name__ == '__main__':
    filein = open("test4.py", "r", encoding="utf-8")
    fileout = open("out4.txt", "w", encoding="utf-8")
    fileout.writelines(["123", "456", "789"])
    fileout.writelines(["\n123\n", "456\n", "789\n"])
    fileout.write("\n\n\n")

    fileout.writelines(filein.readlines())

    filein.close()
    fileout.close()
