
from .models import Profile
from django.contrib.auth.models import User

def save_profile(backend, response,user=None, *args, **kwargs):
    Profile.objects.create(
        addres=user,
        avatar=response['photo'],
    )
    
""" {'access_token': 'fdc518357cf25aa12daef3358c0c25cfff04cf567532fbd086c6a3c6d007ee6d7967d5892d3b3b3e967ef', 
'expires_in': 86400, 
'user_id': 214366260, 
'email': 'chuvachkovik@gmail.com', 
'id': 214366260, 'nickname': '',
 'photo': 
 'https://sun1.userapi.com/sun1-57/s/v1/ig2/C3TIgFnczX0F1fYcGQa3TB2nwq07EJWsoR7nM1rJArONsCGqvcsVa2swPWHL-Q4ZTwbQIO1Hg4D7a2Ts4HjqhSyh.jpg?size=50x50&quality=95&crop=216,356,778,778&ava=1',
  'screen_name': 'anworkjob', 
  'first_name': 'Юрий', 
  'last_name': 'Анциферов', 
  'can_access_closed': True,
   'is_closed': False,
    'user_photo': 
    'https://sun1.userapi.com/sun1-57/s/v1/ig2/C3TIgFnczX0F1fYcGQa3TB2nwq07EJWsoR7nM1rJArONsCGqvcsVa2swPWHL-Q4ZTwbQIO1Hg4D7a2Ts4HjqhSyh.jpg?size=50x50&quality=95&crop=216,356,778,778&ava=1'}
 """