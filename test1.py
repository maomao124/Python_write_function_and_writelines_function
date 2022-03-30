"""
 * Project name(项目名称)：Python_write函数和writelines函数
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:06
 * Version(版本): 1.0
 * Description(描述)：
 file.write(string)
其中，file 表示已经打开的文件对象；string 表示要写入文件的字符串
 """

if __name__ == '__main__':
    file = open("out.txt", "w", encoding="utf-8")
    print(file.writable())
    print(file.write("hello"))
    print(file.write("测试"))
    print(file.write("测试1\n"))
    print(file.write("测试2\n"))
    print(file.write("测试3\n"))
    print(file.write("测试4\n"))

    for i in range(1, 21):
        file.write("输出：" + str(i)+"\n")

    file.close()
