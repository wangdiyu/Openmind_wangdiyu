# 移动APP

class MobileApp:
    def __init__(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    def get_app_info(self):
        print("app_name: %s, download_count: %s, rating: %s" % (self.app_name, self.download_count, self.rating))

    def feature_showcase(self):
        print("这是一个通用的移动应用.")

# 创建社交软件类SocialApp，继承自MobileApp类

class SocialApp(MobileApp):
    def __init__(self, friends_count, supports_short_video, privacy_level):
        self.friends_count = friends_count
        self.supports_short_video = supports_short_video
        self.privacy_level = privacy_level

    def print_info(self):
        print("friends_count: %s, supports_short_video: %s, privacy_level: %s" % (self.friends_count, self.supports_short_video, self.privacy_level))

    def feature_showcase(self):
        print("这是一个社交应用，可以添加好友和发布短视频.")

# 创建游戏应用类GameApp，继承自MobileApp类
   
class GameApp(MobileApp):
    def __init__(self, game_type, multiplayer, in_app_purchases_count):
        self.game_type = game_type
        self.multiplayer = multiplayer
        self.in_app_purchases_count = in_app_purchases_count

    def print_info(self):
        print("game_type: %s, multiplayer: %s, in_app_purchases_count: %s" % (self.game_type, self.multiplayer, self.in_app_purchases_count))
    
    def feature_showcase(self):
        print("这是一个游戏应用，支持多人游戏和内购项目.")

app1 = MobileApp("wechat", 10000000, 5)
app2 = SocialApp("10000", True, "private")
app3 = GameApp("MOBA", "online", 100)
list = [app1,app2,app3]
for i in list:
    i.feature_showcase()
