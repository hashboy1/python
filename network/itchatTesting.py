import itchat
#itchat.login()
itchat.auto_login(hotReload=True)

friends = itchat.get_friends(update=True)
print(type(friends))
#print(friends)



itchat.send(msg="testing message",toUserName='@29922bcab4248090502dd2f18e9f30850c745b77ae8f1bc751d94dcaaf06f50e')
'''
for i in friends:
    NickName = i["NickName"]
    signature = i["Signature"]
    print(NickName)
'''
itchat.logout()