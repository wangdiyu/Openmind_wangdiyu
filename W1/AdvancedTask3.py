# 电影观看计划

def watch_movie_plan(friend_names, movie_list):
    
    for friend_name in friend_names:
        for movie in movie_list:
            movie_dict = {}
            movie_dict[friend_name] = movie
            print(movie_dict)

friend_names = ["张三", "李四", "王五"]
movie_list = ['流浪地球', '复仇者联盟', '哪吒之魔童降世']
watch_movie_plan(friend_names, movie_list)


# ChatGPT的参考答案：

# def create_movie_wishlist(friend_names, movie_list):
#     # 使用 zip 函数将好友名字和电影列表逐一匹配
#     # 创建一个字典，将好友名字映射到他们希望观看的电影
#     wishlist = dict(zip(friend_names, movie_list))
#     return wishlist

# # 示例输入
# friend_names = ['张三', '李四', '王五']
# movie_list = ['流浪地球', '复仇者联盟', '哪吒之魔童降世']

# # 调用函数来创建电影愿望字典
# wishlist = create_movie_wishlist(friend_names, movie_list)

# # 打印结果
# print(wishlist)

