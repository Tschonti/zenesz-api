from django.db import models

# Create your models here.
class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    lyrics = models.CharField(max_length=5000)
    desc = models.CharField(max_length=5000, blank=True, default='')
    verses = models.CharField(max_length=5000, blank=True, default='')
    color = models.CharField(max_length=6, blank=True, default='')

class Search(models.Lookup):
    lookup_name = 'search'

    def as_mysql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return 'MATCH (%s) AGAINST (%s)' % (lhs, rhs), params

models.CharField.register_lookup(Search)
models.TextField.register_lookup(Search)
