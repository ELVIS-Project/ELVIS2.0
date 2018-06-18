from django.db import models
from database.models.custom_base_model import CustomBaseModel
from database.models.part import Part


class Section(CustomBaseModel):
    """A component of a Musical Work e.g. an Aria in an Opera

    Can alternatively be a Musical Work in its entirety.
    A purely abstract entity that can manifest in differing version.
    Can exist in more than one Musical Work.
    Divided into one or more parts.
    Must have at least one part.
    """
    title = models.CharField(max_length=200)
    ordering = models.PositiveIntegerField(null=True)
    parent_sections = models.ManyToManyField('self',
                                             related_name='child_sections',
                                             blank=True)
    parts = models.ManyToManyField(Part, related_name='in_sections')
    contributors = models.ManyToManyField(
            'Person',
            through='ContributedTo',
            through_fields=(
                'contributed_to_section', 'person')
    )

    def __str__(self):
        return "{0}".format(self.title)


    class Meta(CustomBaseModel.Meta):
        db_table = 'section'
