"""Define a Contribution model"""
from django.core.exceptions import ValidationError
from django.db import models

from database.models.custom_base_model import CustomBaseModel
from database.models.contribution_base_model import ContributionBaseModel


class ContributionMusicalWork(ContributionBaseModel):
    """ Relate a person that made a Contribution to a Musical Work/Section/Part.

    The Contribution Model provides a many-to-many relationship with attributes
    between one of Musical Work, Section or Part and Person.

    Each Contribution relates a Person to exclusively one of MusicalWork,
    Section or Part.

    A Musical Work/Section/Part can have many Contributions, since each of
    piece of music can have many contributors with different roles
    i.e. a person composed a piece, two others arranged it, another wrote the
    lyrics.

    Contribution.person : models.ForeignKey
        Reference to a Person that made this Contribution to a Musical Work,
        Section or Part

    Contribution.certainty_of_attribution : models.BooleanField
        Whether it is certain if this Person made this Contribution

    ContributeTo.role : models.CharField
        The role that this Person had in contributing. Can be one of: Composer,
        Arranger, Author of Text, Transcriber, Improviser, Performer

    Contribution.date : postgres.fields.DateRangeField
        The date in which this Contribution happened

    Contribution.location : models.ForeignKey
        Reference to the GeographicArea in which this Contribution happened

    Contribution.contributed_to_work : models.ForeignKey
        Reference to the MusicalWork to which this Contribution was made

    See Also
    --------
    database.models.CustomBaseModel
    database.models.Person
    database.models.MusicalWork
    database.models.Section
    database.models.Part
    database.models.GeographicArea
    """

    person = models.ForeignKey(
        "Person",
        related_name="contributions_works",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
        help_text="The Person that contributed to a Musical Work"
    )

    contributed_to_work = models.ForeignKey(
        "MusicalWork",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="contributions",
        help_text="The Musical Work that the Person contributed to",
    )

    class Meta(CustomBaseModel.Meta):
        db_table = "contribution_musical_work"
        verbose_name_plural = "Contributions to Musical Works"
        verbose_name = "Contribution to Musical Work"

    def __str__(self):
        return "{0}, {1} of {2}".format(
            self.person, self.role.lower(), self.contributed_to_work
        )
