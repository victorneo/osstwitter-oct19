from django.test import TestCase, Client


class TweetsTest(TestCase):
    def test_index(self):
        c = Client()
        response = c.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'Hello, World!')

    def test_greet(self):
        c = Client()

        # test without name
        response = c.get('/greet/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'Hello, World!')

        # test with name
        response = c.get('/greet/nyan/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'Hello, nyan')
