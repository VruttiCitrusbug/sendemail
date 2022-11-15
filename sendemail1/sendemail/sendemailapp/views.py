# from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.conf import settings
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

        # sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        # print(sg)
        # print("*************************************************************************************")
        # response = sg.send(message)








from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Personalization
from django.conf import settings
from python_http_client import exceptions
from sendgrid.helpers.mail import To,Bcc,Cc

TEMPLATE_KEY='d-37a7ab3963d945f48a64c89a52f56de3'
TO_EMAILS = ['saloni.citrusbug@gmail.com']
def sendgrid_mail(to_email=TO_EMAILS, TEMPLATE_KEY=TEMPLATE_KEY, dynamic_data_for_template={'name':'vrutti'}):

    message = Mail()
    message.template_id=TEMPLATE_KEY
    message.from_email = Email(settings.SENDGRID_FROM_MAIL)

    p=Personalization()
    # obj=Email()
    # obj.dynamic_template_data=dynamic_data_for_template 
    # obj.substitutions=[('saloni.citrusbug@gmail.com')]
    # import pdb
    # pdb.set_trace()
    p.add_to(Email('saloni.citrusbug@gmail.com'))

    p.dynamic_template_data = dynamic_data_for_template

    message.add_personalization(p)

    try:
        return HttpResponse("Email Sent to all")
    except exceptions.BadRequestsError as e:
        print("sendgrid error-",e.body)
        pass