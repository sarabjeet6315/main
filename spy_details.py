from datetime import datetime
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name=name
        self.salutation=salutation
        self.age=age
        self.rating=rating
        self.is_online=True
        self.chats=[]
        self.current_status_message=None
spy=Spy('Sarabjeet','Mr.',21,4)
class Chat_Message:
    def __init__(self,message,sent_by_me,id):
        self.message=message
        self.date=datetime.now()
        self.sent_by_me=sent_by_me
        self.id=id
friend_one=Spy('Bikee','Mr.',20,4)
friend_two=Spy('Ansari','Mr.',21,4.2)
friend_three=Spy('Deepak','Mr.',22,4.5)
friends=[friend_one,friend_two,friend_three]