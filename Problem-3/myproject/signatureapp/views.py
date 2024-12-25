import cv2
from django.shortcuts import render, redirect
from .forms import SignatureForm
from .models import Signature

def detect_and_compare_signatures(original_path, uploaded_path):
    # Load the images
    original = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    uploaded = cv2.imread(uploaded_path, cv2.IMREAD_GRAYSCALE)

    # Preprocess: Resize to the same dimensions
    original = cv2.resize(original, (300, 300))
    uploaded = cv2.resize(uploaded, (300, 300))

    # Calculate the difference
    difference = cv2.absdiff(original, uploaded)

    # Compute the similarity score
    similarity = 1 - (cv2.countNonZero(difference) / (300 * 300))
    return similarity * 100  # Return percentage similarity

def upload_signature(request):
    if request.method == 'POST':
        form = SignatureForm(request.POST, request.FILES)
        if form.is_valid():
            signature = form.save()
            original_path = signature.original_image.path
            uploaded_path = signature.uploaded_image.path

            similarity = detect_and_compare_signatures(original_path, uploaded_path)
            return render(request, 'signatureapp/result.html', {'similarity': similarity})
    else:
        form = SignatureForm()
    return render(request, 'signatureapp/upload.html', {'form': form})
