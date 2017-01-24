import json
import os
import uuid

import boto3

from django.conf import settings

from apps.authentication.models import User


def generate_upload_to(instance, filename):
    directory = str(instance.__class__.__name__.lower())
    filename, extension = os.path.splittext(filename)
    filename = str(uuid.uuid4()) + str(extension)
    return '{}/{}/{}'.format(directory, instance.id, filename)


class Email(object):
    def __init__(self, subject, to, context=None, template='default.html', from_email=None, reply_to=None):
        self.subject = subject
        self.template = template
        self.context = context or {}
        self.from_email = from_email or settings.DEFAULT_FROM_EMAIL
        self.reply_to = reply_to or self.from_email

        if isinstance(to, User):
            self.to = [to.email]
        elif isinstance(to, str):
            self.to = [to]
        elif isinstance(to, list):
            self.to = to

    def send(self, force=False):
        message = json.dumps({
            'subject': self.subject,
            'to': self.to,
            'from_email': self.from_email,
            'reply_to': self.reply_to,
            'template': self.template,
            'context': self.context,
        })

        if settings.DEBUG or force:
            sns = boto3.client('sns')
            sns.publish(
                TopicArn='arn:aws:sns:eu-west-1:074761588836:sendEmail',
                Message=message,
                MessageStructure='string'
            )
        else:
            sqs = boto3.resource('sqs')
            queue = sqs.get_queue_by_name(QueueName='v2-sqsEmail')
            queue.send_message(MessageBody=message)
