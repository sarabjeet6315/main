from termcolor import colored
from spy_details import spy,Spy,Chat_Message,friends
from steganography.steganography import Steganography
text=colored("Let's get started",'red')
print text
print "What's up"
Existing=raw_input("Are you Sarabjeet (Y/N)?")
if(Existing=="Y" or Existing=='y'):
      a=2
      while(a==2):
          password=raw_input('Please Enter Your password')
          if(password=='sarab'):
           print 'Welcome To Spy Chat'+ " "+spy.salutation + " "+ spy.name
           print 'your age is'+ " " + str(spy.age)
           print 'your rating is'+ " "+str(spy.rating)
           print 'you are online is' + " "+str(spy.is_online)
           a=4
          else:
           print 'Invalid password'
           print'Re-enter your password'
else:
    print"Enter your details"
    Spy.name=raw_input("What's your name?")
    if len(Spy.name)>0:
       print "valid"
    else:
       print "please again enter the name"
    Spy.salutation=raw_input("what's your gender(Mr. or Mrs.)")
    print 'Welcome' + ' ' + Spy.salutation + ' ' +Spy.name
    Spy.age=0
    Spy.rating=0.0
    Spy.is_online=False
    Spy.age=int( raw_input("What,s your age?"))
    print type(Spy.age)
    if Spy.age>=18 and Spy.age<=50:
         print"VALID"
    else:
         print"INVAlID"
    Spy.rating=float(raw_input("What's Your rating?"))
    if(Spy.rating>4.5):
             print"Outstanding"
    elif(Spy.rating>3.5 and Spy.rating<4.5):
             print"Excllent"
    elif(Spy.rating>2.5 and Spy.rating<3.5):
             print"Good"
    else:
             print"Average"
    Spy.is_online=int(raw_input("1for online "
                        "2 for ofline"))
    if(Spy.is_online==1):
          print "it is online"
    else:
         print"it is ofline"
def start_chat(spy):
    show_Menu=True
    current_status = None
    while show_Menu:
     print'what do you want to do?'
     print '1.Add a status update\n2.Add a New Freinds \n3.Select a friend&Send a secret message\n4.Read a secret message\n5.Read a chat History\n6.Exit'
     Menu_choice=int(raw_input("Menu_choice"))
# For a status update
     if(Menu_choice==1):
         print 'you will chosse for updation'
         def add_status(current_status):
             if (current_status != None):
                 print 'Your current status is' + current_status
             else:
                 print 'There is no current status yet!'
         add_status(current_status)
         default = raw_input('Do you want to chosse from the older status(Y/N)?')
         Status_Message = ('Happy', 'Sad', 'Enjoying','Excited')
         if (default.upper() == 'Y'):
             item_position = 1
             for message in Status_Message:
                 print item_position,message
                 item_position=item_position+1
             choice = int(raw_input('chosse any message'))
             if len(Status_Message) >= choice:
              update_Status_Message = Status_Message[choice-1]
              print 'The Updated Status Message is ' + " " + update_Status_Message
             else:
              print 'please enter a valid number'
              return Status_Message
         elif (default.upper()=='N'):
             new_status_message = raw_input("What status message do you want to set? ")
             if len(new_status_message)>0:
                updated_status_message = new_status_message
                print 'your updated message is'+" " +updated_status_message
             else:
                 print'Re-enter your Status'
                 return new_status_message
#Add a New Friend
     elif Menu_choice==2:
         print('Add a Freind')
         def add_freind():
               new_friend=Spy(' ',' ',0,0.0)
               new_friend.name=raw_input("What\'s your friend name?")
               new_friend.salutation=raw_input('Are they Mr.or Mrs?')
               new_friend.age=int(raw_input('Age?'))
               new_friend.rating=float(raw_input('spy_rating'))
               print 'Welcome to Spy Chat'+' '+new_friend.salutation+ ' '+new_friend.name
               if len(new_friend.name)> 0 and new_friend.age> 12 :
                      print 'CONGRAS New Friend Added!'
               else:
                      print 'Invalid Entry!'
               friends.append(new_friend)
               print new_friend.name
               for temp in friends:

                   print temp.name
         add_freind()
# Select a friend & Send a secret message
     elif Menu_choice==3:
         def select_friend():
             item_number = 0
             for friend in friends:
                 print '%d. %s of aged %d with rating %.2f is online' %(item_number+1,friend.name,friend.age,friend.rating)
                 item_number = item_number + 1
             friend_choice = int(raw_input("Choose from your friend"))
             friend_choice_position=friend_choice-1
             friend_choice_position=int(friend_choice_position)
             return friend_choice_position
         #select_friend()
         def send_message():
             i=select_friend()
             input_path=raw_input('enterimage path')
             message=raw_input('write your text')
             output_path="C:\Users\Sarabjeet Singh\Desktop\sarab.jpg"
             Steganography.encode(input_path,output_path,message)
             a=Chat_Message(message,True,i)
             spy.chats.append(a)
         send_message()
#Read a secret message
     elif Menu_choice==4:
         i=select_friend()
         output_pat=raw_input("enter the image path")
         text=Steganography.decode(output_pat)
         print text
         a=Chat_Message(text,False,i)
         spy.chats.append(a)
#Read a chat history
     elif Menu_choice==5:
         def read_chat_history():
             read_for = select_friend()
             for Chat in spy.chats:
                 if Chat.id == read_for:
                     if Chat.sent_by_me == True:
                         print colored('%s'%Chat.date,'blue')
                         print colored('you said','red'),
                         print ('%s'%Chat.message)
                     else:
                         print colored('[%s]' %Chat.date,'blue' )
                         print colored(friends[read_for].name,'red'),
                         print ('%s'%Chat.message)
         read_chat_history()
     else:
         show_Menu=False
         print 'Exit'
start_chat(spy)