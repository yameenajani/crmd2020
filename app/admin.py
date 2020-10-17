from django.contrib import admin
from .models import Debate, Score, CalculatedScore

admin.site.site_header = 'CRMD 2020'
admin.site.site_title = 'CRMD 2020'
admin.site.index_title = 'CRMD 2020'

# Register your models here.
admin.site.register(Debate)
admin.site.register(Score)
admin.site.register(CalculatedScore)

"""
Admin - 
yameen
1234
"""

"""
Team - 
CRMD1
@Testuser
"""

"""
Team - 
CRMD2
@Testuser
"""
