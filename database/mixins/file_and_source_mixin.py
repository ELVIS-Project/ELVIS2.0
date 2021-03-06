from django.apps import apps
from django.db.models import QuerySet


class FileAndSourceMixin:
    source_instantiations: QuerySet

    @property
    def files(self) -> QuerySet:
        file_model = apps.get_model("database", "file")
        files = file_model.objects.filter(
            id__in=self.source_instantiations.all().values_list("files", flat=True)
        )
        return files

    @property
    def sources(self) -> QuerySet:
        source_model = apps.get_model("database", "source")
        sources = source_model.objects.filter(
            id__in=self.source_instantiations.all().values_list("source", flat=True)
        )
        return sources

    @property
    def files_count(self) -> QuerySet:
        count = self.files.count()
        return count
