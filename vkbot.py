import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
def write_msg(user_id, message):
    vk.method('messages.send', {'type': 'confirmation', 'group_id': 177329543})


token = "b76a32e972f618e9b066b0f637bdb33178c9c1bff79ba99620032cb54debea334b0072a2d940363711409"


vk = vk_api.VkApi(token=token)


longpoll = VkLongPoll(vk)


for event in longpoll.listen():

    
    if event.type == VkEventType.MESSAGE_NEW:
    
        
        if event.to_me:
        
            
            request = event.text
            
            
            if request == "hi":
                write_msg(event.user_id, "hi")
            elif request == "spok":
                write_msg(event.user_id, "bye((")
            elif request == "":
                write_msg(event.user_id, "bye((")
            else:
                write_msg(event.user_id, "Shut up bitch...")
