import datetime
from django.db.models.signals import post_save, pre_save, m2m_changed, post_init
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import Post, Comment
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib.auth.models import User


@receiver(post_save, sender=Comment)
def send_mail_resp(sender, instance, created, **kwargs):
    if created:
        user = Post.objects.get(pk=instance.post_id).user
        send_mail(
            subject='Новый отклик',
            message=f'{instance.user} оставил отклик на Ваше обьявление: {instance.text}',
            from_email='yamargoshka15@gmail.com',
            recipient_list=[User.objects.filter(username=user).values("email")[0]['email']],
        )

'''
@receiver(m2m_changed, sender=Post)
def notify_subscribers(instance, action, *args, **kwargs):
    time_delta = datetime.timedelta(7)
    start_date = datetime.datetime.utcnow() - time_delta
    end_date = datetime.datetime.utcnow()

    posts = Post.objects.filter(post_data__range=(start_date, end_date))

    for category in Category.objects.all():
        html_content = render_to_string('account/email/week_email.html',
                                        {'posts': posts, 'category': category}, )
        msg = EmailMultiAlternatives(
            subject=f'"Еженедельная подписка (celery)"',
            body="Новости",
            from_email='yamargoshka15@gmail.com',
            to=category.get_subscribers_emails())
        msg.attach_alternative(html_content, "text/html")
        msg.send()'''