# views.py
import os
from django.shortcuts import render, redirect
import pandas as pd
from django.conf import settings
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            return redirect('data_analysis', file_name=file.name)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


import os
from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def data_analysis(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    df = pd.read_csv(file_path)

    # Display first few rows of data
    head = df.head().to_html()

    # Calculate summary statistics
    desc = df.describe().to_html()

    # Handle missing values
    missing_values = df.isnull().sum().to_dict()

    # Generate plots
    plt.figure(figsize=(10, 4))
    sns.histplot(df.select_dtypes(include=[np.number]).dropna(), kde=True)
    sns.histplot(df['Period'], bins=15, kde=True)  # Adjust 'bins' as needed

    plt.title('Histogram of Data Values')
    plt.xlabel('Period')
    plt.ylabel('Data Values')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    image_base64 = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'analysis.html', {
        'head': head,
        'desc': desc,
        'missing_values': missing_values,
        'plot': image_base64,
    })
plt.show()