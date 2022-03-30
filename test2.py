"""
 * Project name(项目名称)：Python_write函数和writelines函数
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 13:12
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    file = open("out2.txt", "a", encoding="utf-8")
    print(file.writable())
    print(file.write("hello"))
    print(file.write("测试"))
    print(file.write("测试1\n"))
    print(file.write("测试2\n"))
    print(file.write("测试3\n"))
    print(file.write("测试4\n"))

    for i in range(1, 21):
        file.write("输出：" + str(i) + "\n")

    file.close()
