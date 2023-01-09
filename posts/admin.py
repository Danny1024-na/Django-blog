from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post,Category

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    'to edit in admin Page'
    list_display =['title','author','tags']
    list_filter =['author','tags']
    search_fields =['title','content']

admin.site.register(Post,PostAdmin)
# admin.site.register(Chefs,PostAdmin)
# admin.site.register(Client,PostAdmin)


'to change the title of the page'
'we can also edit the thems of the admain page , simply search in google'
#admin.site.site_header = 'My Blog (Danny21)'