# django_sleep
Django middleware to create a delay in loading pages for debug purpose (or any other reasons)

# Usage 

In the **settings.py** file, key **SLEEP_TIME = x** define sleep time in second.

# Installation

If not existing : create a folder 
> yourproject/yourapp/middleware

Put the django_sleep.py file into.

Add the middleware in your **settings.py** file.

> MIDDLEWARE = [
>    'corsheaders.middleware.CorsMiddleware',
>    ....
>>    'project.middleware.django_sleep.SleepMiddleware',
> ]

Add timing (example 2 seconds) by adding SLEEP_TIME = 2 key in  **settings.py**
> SLEEP_TIME = 2

That's it !
