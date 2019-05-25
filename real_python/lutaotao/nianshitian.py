class 念诗类():
    一首诗 = ['《卜算子》', '我住长江头，', '君住长江尾。', '日日思君不见君，', '共饮长江水。']

    @classmethod
    def 念诗函数(cls):
        cls.用户名 = input('请输入你想给谁念诗：')
        print(f'念给{cls.用户名}的诗：')
        for i in cls.一首诗:
            print(i)

if __name__ == '__main__':
    念诗类.念诗函数()
