## baid-wagtail

Some resources:

- https://docs.wagtail.org/

To create a new page:

```
python manage.py startapp <name>
```

For example:

```
python manage.py startapp news
```


## API

- Query pages: 
  
  GET `/api/v2/pages?<?>=<?>`


- Get page data:

  GET `/api/v2/pages/<id>`

  Examples:

  - GET `/api/v2/pages/3`

    ```json
    {
    "id": 3,
    "meta": ...,
    "title": "Home",
    "head": "欢迎来到北京中学国际部!",
    ...
    }
    ```
