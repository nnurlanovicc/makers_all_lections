from django.core.mail import send_mail


def send_activation_code(email,activation_code):
    message = f'''
        вы успешно зарегались на нашем сайте. пройдите активацию аккаунта, отправивнам этот код:  {activation_code}
    '''
    send_mail(
        'активация аккаунта',
        message,
        'test@gmail.com',
        [email]
    )


    