from django.forms import CharField, DateField
from django.test import TestCase
from .models import Show
from django.contrib.auth.models import User
from django.test import Client



class UserTestCase(TestCase):
    def setUp(self):
        self.username = 'testusername'
        self.password = 'HelloPassword123'

    def test_signup(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    def test_signup_form(self):
        response = self.client.post("/accounts/signup/", data={
            'username': self.username,
            'password1': self.password,
            'password2': self.password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/shows/")
    
    def testLogout(self):
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/")

    

class LoginTestCase(TestCase):    
    def setUp(self):
        self.username = 'testusername'
        self.password = 'Password123'
        user = User.objects.create_user(username=self.username, password=self.password)
        self.assertTrue(user.is_active)

    def test_login(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/login.html')

    def test_login_form(self):
        response = self.client.post("/accounts/login/", data={
            'username': self.username,
            'password': self.password
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, "/")
        

class ShowTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testusername')
        user.set_password('Password123')
        user.save()
        print("???????")
        print("jenkins test")
        loggedin = Client.login(username='testusername', password='Password123')
        print("???", loggedin)

    def test_show(self):
        response = self.client.get("/shows/create/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='show_form.html')