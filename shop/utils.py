from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from transliterate import detect_language
from transliterate import slugify as slugify_translit
from django.utils.text import slugify


def autoslug(fieldname):
    def decorator(model):

        assert hasattr(model, fieldname), f"{fieldname} does not exist"
        assert hasattr(model, 'slug'), f"Model doesn't have any slug"

        @receiver(pre_save, sender=model, weak=False)
        def generate_slug(sender, instance, *args, **kwargs):
            if not instance.slug:
                source = getattr(instance, fieldname)
                lang = detect_language(source)
                str_ = get_random_string()
                if lang:
                    slug = slugify_translit(source, lang)
                    instance.slug = slug + str_
                else:
                    slug = slugify(source, allow_unicode=True)
                    instance.slug = slug + str_
        return model
    return decorator
