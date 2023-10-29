# 初始化APP

class MobileApp:
    def __init__(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    def get_app_info(self):
        print("app_name: %s, download_count: %s, rating: %s" % (self.app_name, self.download_count, self.rating))

app_name = input("请输入App名：")
download_count = int(input("请输入下载量："))
rating = int(input("请输入评分："))
app1 = MobileApp(app_name, download_count, rating)
app1.get_app_info()
