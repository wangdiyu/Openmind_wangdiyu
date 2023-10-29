# 移动APP

class MobileApp:
    def __init__(self, app_name, download_count, rating):
        self.app_name = app_name
        self.download_count = download_count
        self.rating = rating

    def get_app_info(self):
        print("app_name: %s, download_count: %s, rating: %s" % (self.app_name, self.download_count, self.rating))

# 创建社交软件类SocialApp，继承自MobileApp类

class SocialApp(MobileApp):
    def __init__(self, friends_count, supports_short_video, privacy_level):
        self.friends_count = friends_count
        self.supports_short_video = supports_short_video
        self.privacy_level = privacy_level

    def print_info(self):
        print("friends_count: %s, supports_short_video: %s, privacy_level: %s" % (self.friends_count, self.supports_short_video, self.privacy_level))

# 创建游戏应用类GameApp，继承自MobileApp类
   
class GameApp(MobileApp):
    def __init__(self, game_type, multiplayer, in_app_purchases_count):
        self.game_type = game_type
        self.multiplayer = multiplayer
        self.in_app_purchases_count = in_app_purchases_count

    def print_info(self):
        print("game_type: %s, multiplayer: %s, in_app_purchases_count: %s" % (self.game_type, self.multiplayer, self.in_app_purchases_count))
    
app1 = SocialApp(friends_count=10000,supports_short_video=True, privacy_level="private")
app1.print_info()
app2 = GameApp(game_type="MOBA", multiplayer="online", in_app_purchases_count=100)
app2.print_info()