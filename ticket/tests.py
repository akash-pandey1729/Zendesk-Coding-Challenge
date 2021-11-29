from django.test import TestCase
import ticket.views as views

# Create your tests here.
class UnitTesting(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 30 tickets for pagination test
        views.auth = True
        views.length = 30
        for ticket_id in range(views.length):
            views.tickets.append({'subject' : 'Test Ticket', 'description' : 'This is a test description!'})

    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_about_url_exists_at_desired_location(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_logout_url_exists_at_desired_location(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_login_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_ticket_url_exists_at_desired_location(self):
        for index, ticket in enumerate(views.tickets):
            response = self.client.get(f'/home/{index}')
            self.assertEqual(response.status_code, 200)

    def test_home_url_uses_correct_template(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket/home.html')

    def test_about_url_uses_correct_template(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket/about.html')

    def test_logout_url_uses_correct_template(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/logout.html')

    def test_login_url_uses_correct_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_ticket_url_uses_correct_template(self):
        for index, ticket in enumerate(views.tickets):
            response = self.client.get(f'/home/{index}')
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'ticket/individual_ticket.html')

    def test_ticket_url_displays_correct_ticket(self):
        for index, ticket in enumerate(views.tickets):
            response = self.client.get(f'/home/{index}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['ticket'], ticket)

    def test_home_page_is_paginated(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)

    def test_first_page_is_paginated_by_twenty_five(self):
        response = self.client.get('/home/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['tickets']), 25)

    def test_second_page_exists_at_desired_location(self):
        response = self.client.get('/home/?page=2')
        self.assertEqual(response.status_code, 200)

    def test_first_page_context(self):
        response = self.client.get('/home/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'home')
        self.assertEqual(response.context['auth'], True)
        self.assertEqual(response.context['length'], 30)
        self.assertTrue('page_obj' in response.context)
        self.assertTrue('tickets' in response.context)

    def test_about_context(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['title'], 'about')
        self.assertEqual(response.context['auth'], True)