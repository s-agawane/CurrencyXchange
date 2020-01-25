from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Wallet_test(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

    def testcase1(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/wallet/view/' ,HTTP_AUTHORIZATION='Token {}'.format(self.token))
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def testcase2(self):
        self.client.force_login(user=self.user)
        response = self.client.post('/wallet/deposit/' , data={"amount": 1000}, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def testcase3(self):
        self.client.force_login(user=self.user)
        response = self.client.post('/wallet/withdraw/' , data={"amount": 50}, HTTP_AUTHORIZATION='Token {}'.format(self.token))
        print(response.data)
        self.assertEqual(response.status_code, 200)