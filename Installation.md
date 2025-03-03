## Steps to run project with the traditional method

# este es un ejemplo ir complentando

1. Clone the repo
    ```sh
        git clone https://github.com/JoaquiinAguilar/API-REST-PERSONAS.git
    ```
2. Access into the folder 
    `cd `
3. Create an virtual environment 
    `python3 -m venv .env`
4. Activate the virtual environment 
    `source .env/bin/activate`
5. Update pip to latests version
    `pip install --upgrade pip`
6. Install libraries
    `pip install -r requirements.txt --no-cache`
7. Create file .env inside **** folder, copy the content from **.env.example** and change the database connection values
8. Run migrations: `python manage.py migrate`
9. Execute python project
    `python manage.py runserver 8090`
10. Go to the explorer and navigate to `http://localhost:8080`
11. Read the instructions, make your solution and **Good look!**