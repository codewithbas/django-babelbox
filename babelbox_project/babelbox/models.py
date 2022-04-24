from django.db import models
from django.conf import settings


class Message(models.Model):
    """This model represents the original user input."""
    class Meta:
        ordering =['-created_at']
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=255)
    message_language = models.CharField(max_length=2, choices=((lang_id, flag) for flag,lang_id,_ in settings.TRANSLATED_LANGUAGES))
    message = models.TextField()

    def translations(self, language):
        return self.translated_messages.filter(language=language)


class TranslatedMessage(models.Model):
    """This model contains the translated message."""
    class Meta:
        """Model Meta options"""
        unique_together = ['message', 'language']
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="translated_messages")
    language = models.CharField(max_length=2, choices=((lang_id, flag) for flag,lang_id,_ in settings.TRANSLATED_LANGUAGES))
    translated_message = models.TextField()