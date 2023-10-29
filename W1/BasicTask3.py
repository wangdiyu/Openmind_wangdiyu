# 点外卖

def order_food(food_name,location):
    
    if food_name == "1":
        return "您选择了快餐类，" + " 30分钟内送达您的地址：" + location
    elif food_name == "2": 
        return "您选择了火锅类，" + " 1小时内送达您的地址：" + location
    else:
        return "您选择了其他，" + " 45分钟内送达您的地址：" + location
    
food_name = input("今天您想吃点啥？ 1.快餐类； 2.火锅类； 3.其他 >>> ")
location = input("请输入您的地址 >>> ")
print(order_food(food_name, location))
