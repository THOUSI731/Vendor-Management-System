##  Instructions to Run the Code


1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/THOUSI731/Vendor-Management-System.git

2. Create a Virtual Environment:

   ```bash
    python -m venv venv
    #for windows
    venv\Scripts\activate

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt

5. Create SuperUser and Runserver;

    ```bash
    python manage.py makemigrations
    python manage.py migrate    
    python manage.py createsuperuser
    python manage.py runserver
    
6. For Api Documentation
    ```bash
    http://localhost:8000/swagger/
