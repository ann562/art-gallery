from django.contrib import admin
from hello.models import ArtPiece, Feedback


class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0
    readonly_fields = ('name', 'email', 'rating', 'comment', 'created_at')
    can_delete = True
    fields = ('name', 'email', 'rating', 'comment', 'created_at')
    
    def has_add_permission(self, request, obj=None):
        return False

@admin.register(ArtPiece)
class ArtPieceAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'medium', 'year_created', 'price', 'average_rating', 'total_ratings')
    list_filter = ('artist', 'medium', 'year_created')
    search_fields = ('title', 'artist', 'description')
    inlines = [FeedbackInline]
    
    fieldsets = (
        ('Artwork Information', {
            'fields': ('title', 'artist', 'description', 'image')
        }),
        ('Details', {
            'fields': ('year_created', 'medium', 'price')
        }),
    )

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('art_piece', 'name', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('name', 'comment', 'art_piece__title')
    readonly_fields = ('created_at',)