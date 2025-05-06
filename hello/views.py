from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from .models import ArtPiece, Feedback
from .forms import FeedbackForm

def art_piece_list(request):
    art_pieces = ArtPiece.objects.all().order_by('-created_at')
    return render(request, 'gallery/art_piece_list.html', {'art_pieces': art_pieces})

def art_piece_detail(request, pk):
    art_piece = get_object_or_404(ArtPiece, pk=pk)
    feedback_list = art_piece.feedback_set.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.art_piece = art_piece
            feedback.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('art_piece_detail', pk=art_piece.pk)
    else:
        form = FeedbackForm()

    return render(request, 'gallery/art_piece_detail.html', {
        'art_piece': art_piece,
        'feedback_list': feedback_list,
        'form': form
    })

@login_required
def feedback_report(request):
    art_pieces = ArtPiece.objects.annotate(
        avg_rating=Avg('feedback__rating'),
        num_ratings=Count('feedback')
    ).order_by('-avg_rating')

    return render(request, 'gallery/feedback_report.html', {
        'art_pieces': art_pieces,
    })
