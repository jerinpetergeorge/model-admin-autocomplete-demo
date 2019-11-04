
# model-admin-autocomplete-demo

## How to use?
1. clone the repository
2. install the dependencies using `requirements.txt` file
```pip install -r requirements.txt``` 
3. migrate the database
```python manage.py migrate```
4. create a superuser
```python manage.py createsuperuser```
5. load test data into database
```python manage.py loaddata  data_fixture.json --app app_one --format json```
6. run Django development server
```python manage.py runserver```
7. go to Django admin and head into the url, [http://localhost:8000/admin/app_one/article/add/](http://localhost:7777/admin/app_one/article/add/)
8. That's it
