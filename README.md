# csv_analysis_assignment

To fulfill all the requirements let's begin with step by step.
STEP 1: SET UP DJANGO 
To set up Django environment You need to have Python installed and use pip to install Django. That i already have it in my system So I will directly start with creating the application 
To install Django we can use the command "pip install Django" 
1. To create the application
![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/9e520912-63ff-4d0b-884f-2d162f50d4e6)

2. To start the application
   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/f9e148c0-e01f-4967-96a3-47809069899a)

This is how the folder structure looks like

   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/fe71e6ec-6176-41df-b03b-eac644679171)

3. In csv_analysis_project/settings.py, add csv_analysis to the INSTALLED_APPS list.
  ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/4e01c81d-847c-4599-9667-a05b11f50302)

This is how we created the environment of django, now it's ready to add the features 

STEP 2: ADD FILE UPLOADING 

1. created a file forms.py in csv_analysis and using forms module we can upload file
   
   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/f740d771-acd0-4c6f-8241-e1d114b3b076)

2. We will define model for this
   
   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/bfb853de-709d-41b9-93ff-4366356fd2c1)

3. We will include the path

   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/e43f88a2-2910-4864-acc0-12daa7229a8b)

4. Created the urls.py file to define the urls

   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/37b1e2b0-a163-4037-a4d9-b40bb011e825)

5. Now i have installed all the dependencies and creating the view for files
   
   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/abe40387-22c8-4806-827e-6fcfc2eb5dd8)


STEP 3: DATA PROCESSING

1. installing matplotlib and seaborn for view
   
from django.shortcuts import render
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def data_analysis(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    df = pd.read_csv(file_path)

    head = df.head().to_html()
    
    desc = df.describe().to_html()

    missing_values = df.isnull().sum().to_dict()

    plt.figure(figsize=(10, 4))
    sns.histplot(df.select_dtypes(include=[np.number]).dropna(), kde=True)
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

    2. Now ,Added the url pattern 
    urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('analysis/<str:file_name>/', views.data_analysis, name='data_analysis'),
]

2. adding the path in urls
   urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    path('analysis/<str:file_name>/', views.data_analysis, name='data_analysis'),
]


STEP 4 : DATA VISUALIZATION

1. Generate plots:
Used matplotlib and seaborn to generate plots as demonstrated in the data_analysis view.

STEP 5: INTERFACE

1. created templates folder
2. Added html file upload.html

   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/f22a1f53-0419-465d-926a-edcb7a5642ae)

3. Add another html file analysis.html
   
   ![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/fd521088-aea3-443d-b223-b0cccb4a7b76)


STEP 6 : CONFIGURATION

1. Adding media configuration in settings.py
   
![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/9956ff2b-682a-45d7-891a-20f2f2f514ce)

2. In csv_analysis_project/urls.py, add media URL configuration.
![image](https://github.com/Foramsp/csv_analysis_assignment/assets/87531019/6618887c-a6e5-4ae4-b243-d0f5e17ef55a)








   








