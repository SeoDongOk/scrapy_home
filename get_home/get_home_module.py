from django.core.mail import send_mail
from django.http import HttpResponse


def send_gmail(df):
    homeList=df
    homeList_html = homeList.to_html(index=False)  
    subject = '청년주택 추가 모집 공고 떳다!'
    message = homeList_html
    recipient_list = ['hcan1445@gmail.com']  # 받는 사람 이메일 주소
    from_email = 'hcan1445@gmail.com'
    try:
        send_mail(subject, message, from_email, recipient_list,fail_silently=False,html_message=homeList_html)
        return HttpResponse('Email sent successfully')
    except Exception as e:
        return HttpResponse(f'Error sending email: {str(e)}')
