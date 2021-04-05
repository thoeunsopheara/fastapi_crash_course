
# FastAPI crash course with Bitfumes

### This is fastapi crash course I learn from bitfumes youtube channel

- #### Watch video on [YouTube](https://www.youtube.com/watch?v=7t2alSnE2-I)

  main.py file on top level is for course intro

  Blog application is on blog/ folder

  Clone this repository:
  ```
    git clone https://github.com/thoeunsopheara/fastapi_crash_course.git
  ```
  or using ssh
  ```
    git clone git@github.com:thoeunsopheara/fastapi_crash_course.git
  ```

-  #### Create virtual env
  ```
    cd fastapi_crash_course
    python -m venv venv
  ```
  or using virtualenv
  ```
    virtualenv venv
  ```
- #### Activate virtualenv
  on windows
  ```
    venv\Scripts\activate
  ```
  on mac and linux
  ```
    source venv/bin/activate
  ```
- #### Install library

  ```
    pip install -r requirements.txt
  ```

- #### Start server
  ```
    uvicorn blog.main:app --reload
  ```

  --reload for reload app every time .py file saved. You can start server without it.

- #### View in webpage
  ###### Go to http://127.0.0.1:8000/docs and http://127.0.0.1:8000/redoc for your api documentation

## Contact me:
  - Email: [thoeun.sopheara@gmail.com](mailto:thoeunsopheara@gmail.com)


# Don't forget give a start on this repository
