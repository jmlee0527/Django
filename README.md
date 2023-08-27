# Django

## Django 환경 설치 (mac)

1. 가상환경 생성


    python -m venv [가상환경 명]     

2. 가상환경 활성화 

    source [가상환경명]/bin/activate

3. Django 설치

    pip install django

4. 프로젝트 생성

    django-admin startproject [프로젝트명]

5. 생성한 프로젝트 디렉터리로 이동

6. 어플리케이션 생성

    python manage.py startapp [어플리케이션 이름]

7. setting.py 에 install_app 에 추가

<hr/>

* admin 계정 생성
    python manage.py createsuperuser

* 회원가입 extenstion
    pip install django-allauth

* 소셜 로그인 기능
    pip install social-auth-app-django

* bootstrap 추가
    pip install bootstrap4