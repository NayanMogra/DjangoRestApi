# DjangoRestFramework

## Django Article
Django Article is a simple DjangoRestFrame work implemantion to add article title ,article date, username and useremail.
Follow the Steps to use DjangoRestApi

****
## Local installation guide:
**Clone the repository**
```bash
 git clone https://github.com/NayanMogra/DjangoRestApi.git
```

**Install virtual enviornment**
*For Windows*
```bash
python -m pip install --user enviroment
python -m venv env
python -m enviroment --help
```
*For Linux*
```bash
python3 -m pip install --user virtualenv
python3 -m venv env
python -m enviroment --help
```

**Activate the  virtual enviornment**
*For Windows*
```bash
cd flaskblog\enviornment
Scripts\activate
```
*For Linux* 
```bash
source env/bin/activate
```

****
## Installing dependencies
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies in blog directory

### To install all dependencies at once use 
*For both Windows and Linux*
```bash
pip install -r requirement
```

## Run the code at your local envn
**Run it as**
```bash
 python manage.py runserver
 ```
>Open your browser/postman and the site can be found running at http://127.0.0.1:8000/

**To get all the article set a, GET request on link**
>  http://127.0.0.1:8000/article/

**To add a article set a, POST request on link with credentials**
>  http://127.0.0.1:8000/article/

**To see particular article set a, GET request on link with article id**
>  http://127.0.0.1:8000/detail/<id>

**To update particular article set a, PUT request on link with article id**
>  http://127.0.0.1:8000/detail/<id>

**To delete particular article set a, DELETE request on link with article id**
>  http://127.0.0.1:8000/detail/<id>

