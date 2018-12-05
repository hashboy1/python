Prefer = {"jim": {"War": 1.9, "the big bang": 1.0, "The lord of wings": 4.0, "Beautiful America": 4.7},
          "lily": {"War": 2.0, "Kongfu": 4.1, "The lord of wings": 3.6},
          "tommy": {"War": 2.3, "Kongfu": 5.0, "The lord of wings": 3.0},
          "jack": {"War": 2.8, "Kongfu": 5.5, "The lord of wings": 3.5}}


# 欧式距离及几何距离，有m个物品就有m维度的空间，把用户u定位到这个m维度的空间里
# 用户u在m维度空间里的第i维度的坐标值表示用户对此物品的评分
# 这里只计算2维度的情况
def EuclidDistance(prefer, person1, person2):
    sim = {}
    for item in prefer[person1]:
        if item in prefer[person2]:
            sim[item] = 1  # 添加共同项到字典中
    # 无共同项，返回0
    if len(sim) == 0:
        return 0
        # 计算所有共有项目的差值的平方和
    sum_all = sum([pow(prefer[person1][item] - prefer[person2][item], 2) for item in sim])
    # 返回改进的相似度函数，距离越大相似度越小
    # 两个点完全重合相似度为1
    return 1 / (1 + (sum_all ** 0.5))


# 测试
print("\n欧氏距离表示相似度....")
print("EuclidDistance(Prefer,'tommy','jim') = ", EuclidDistance(Prefer, 'tommy', 'jim'))
print("EuclidDistance(Prefer,'tommy','lily') = ", EuclidDistance(Prefer, 'tommy', 'lily'))
print("EuclidDistance(Prefer,'tommy','jack') = ", EuclidDistance(Prefer, 'tommy', 'jack'))