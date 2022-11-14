# from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
# from django.conf import settings
# # Create your views here.
# def index(request):
#     if request.method=='POST':
#         name=request.POST['name']
#         print(name)
#         print(settings.DEFAULT_FROM_EMAIL)
#         try:
#             send_mail(subject='responding form',
#             message="hello {}".format(name),
#             from_email=settings.DEFAULT_FROM_EMAIL,
#             recipient_list=['jayendra.citrusbug@gmail.com'],
#             fail_silently=False)
#         except Exception as e:
#             print(e, "***************")
#         print("*********************************************************************************************")
#         return redirect('/mailsuccess')
#     return render(request,'index.html')
# def mailsuccess(request):
#     return HttpResponse("checkout email")


from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Personalization
from django.conf import settings
from python_http_client import exceptions
from sendgrid.helpers.mail import To,Bcc,Cc
# def sendgrid_mail(to_email, TEMPLATE_KEY, dynamic_data_for_template):
#     message = Mail(from_email=settings.SENDGRID_FROM_MAIL,
#                     to_emails=to_email,)
#     message.dynamic_template_data=dynamic_data_for_template
#     message.template_id=TEMPLATE_KEY
#     try:
#         sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
#         response = sg.send(message)
#         print(response.status_code)
#         print(response.body)
#         print(response.headers)
#         return response
#     except exceptions.BadRequestsError as e:
#         print("sendgrid error-",e.body)
#         pass

# FROM_EMAIL = 'vrutti.citrusbug@gmail.com'
TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3'
TO_EMAILS = ['jayendra.citrusbug@gmail.com']
def sendgrid_mail(to_email, TEMPLATE_KEY=TEMPLATE_KEY, dynamic_data_for_template={'name':'vrutti'}):
    message = Mail(from_email=settings.SENDGRID_FROM_MAIL,
                    to_emails=['dhiren.citrusbug@gmail.com','abc1@yopmail.com','jayendra.citrusbug@gmail.com','saloni.citrusbug@gmail.com'],
                    subject="Test Email",
                    html_content="hello")
    message.dynamic_template_data=dynamic_data_for_template
    message.template_id=TEMPLATE_KEY
    try:
        # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        # print(sg)
        # print("*************************************************************************************")
        # response = sg.send(message)
        return HttpResponse("Email Sent to all")
    except exceptions.BadRequestsError as e:
        print("sendgrid error-",e.body)
        pass