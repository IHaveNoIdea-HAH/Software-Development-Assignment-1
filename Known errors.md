# Known Errors:

## Failed to start

I have no idea why this happens. But sometimes when running the python file it causes this error to occur.

<img width="1554" height="253" alt="image" src="https://github.com/user-attachments/assets/7a331285-b09a-489b-b4e3-b27f214ccc09" />

### Temporary Fix:

Running the program again and again until it works somehow fixes it. Not a permanent fix.


## Homepage fail to load

Probably something to do with the code
see if app>__init__.py
line 8 says

```
def create_app(current_folder):
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
```
<img width="855" height="138" alt="image" src="https://github.com/user-attachments/assets/3fd8d812-6eff-4fc9-8b5e-34363fe8625d" />

## images suddenly failing to load in the homepage
<img width="1846" height="976" alt="image" src="https://github.com/user-attachments/assets/fad34a84-59a1-43b8-9330-1bdb00dfd4b0" />
