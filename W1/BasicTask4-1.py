# 移动APP

class MobileApp:
    def __init__(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    def get_app_info(self):
        print("app_name: %s, download_count: %s, rating: %s" % (self.app_name, self.download_count, self.rating))

wechat = MobileApp("WeChat", 10000000, 5.0)
qq = MobileApp("QQ", 10000000, 5.0)
wechat.get_app_info()
qq.get_app_info()