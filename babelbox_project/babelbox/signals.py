import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Message, TranslatedMessage






@receiver(post_save, sender=Message)
def my_handler(sender, instance, **kwargs):
    # target_languages = [lang_id.lower() for _,lang_id,_ in settings.TRANSLATED_LANGUAGES if lang_id != instance.message_language]
    target_languages = [lang_id.lower() for _,lang_id,_ in settings.TRANSLATED_LANGUAGES]

    # # Create Pseudo-Translation from original message
    # translation = TranslatedMessage(
    #         message=instance,
    #         language=instance.message_language,
    #         translated_message=instance.message
    #     )
    # translation.save()

    request = requests.post(settings.AZURE_ENDPOINT + '/translate',
                            params={
                                'api-version': '3.0',
                                'from': instance.message_language.lower(),
                                'to': target_languages
                            },
                            headers={'Ocp-Apim-Subscription-Key': settings.AZURE_KEY_1},
                            json=[{
                                'text': instance.message
                            }])
    translations = request.json().pop().get('translations', [])
    for translation in translations:
        translation_object = TranslatedMessage(
            message=instance,
            language=translation.get('to').upper(),
            translated_message=translation.get('text')
        )
        translation_object.save()

