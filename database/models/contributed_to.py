from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import DateRangeField
from database.models.custom_base_model import CustomBaseModel
from database.models.person import Person
from database.models.geographic_area import GeographicArea


class ContributedTo(CustomBaseModel):
    """Relates a person that contributed to a work/section/part

    A work/section/part can have many contributors with different roles
    i.e. a person composed a piece, two others arranged it, another wrote the
    lyrics
    A person can be related to a work, section or part, this is implemented
    using GenericForeignKeys
    """
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, null=False, blank=False,
                            default='Composer')
    date = DateRangeField()
    location = models.ForeignKey(GeographicArea, on_delete=models.SET_NULL,
                                 null=True)

    # Generic foreign key to allow polymorphic relation to work/section/part
    limit = models.Q(app_label='database', model='musicalwork') | models.Q(
            app_label='database', model='section') | models.Q(
            app_label='database', model='part')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to=limit)
    object_id = models.PositiveIntegerField()
    contributed_to = GenericForeignKey('content_type', 'object_id')


    class Meta(CustomBaseModel.Meta):
        db_table = 'contributed_to'