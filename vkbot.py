def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API-���� ��������� �����
token = "6a9c267cd469388709a9e9acaddbe0aa81a0abbf12239b3e597a31729ffbddb9c88e80a443554c918b8f7"

# ������������ ��� ����������
vk = vk_api.VkApi(token=token)

# ������ � �����������
longpoll = VkLongPoll(vk)

# �������� ����
for event in longpoll.listen():

    # ���� ������ ����� ���������
    if event.type == VkEventType.MESSAGE_NEW:
    
        # ���� ��� ����� ����� ��� ����( �� ���� ����)
        if event.to_me:
        
            # ��������� �� ������������
            request = event.text
            
            # �������� ������ ������
            if request == "������":
                write_msg(event.user_id, "���")
            elif request == "����":
                write_msg(event.user_id, "����((")
            else:
                write_msg(event.user_id, "�� ������ ������ ������...")