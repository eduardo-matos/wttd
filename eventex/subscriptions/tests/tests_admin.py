from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkAsPaid(TestCase):
	def setUp(self):
		self.model_admin = SubscriptionAdmin(Subscription, admin.site)

		Subscription.objects.create(name='Eduardo', cpf='11122233345', email='edu@matos.com')

	def test_has_action(self):
		self.assertIn('mark_as_paid', self.model_admin.actions)

	def test_mark_all(self):
		fake_request = Mock()
		queryset = Subscription.objects.all()
		self.model_admin.mark_as_paid(fake_request, queryset)

		self.assertEqual(1, Subscription.objects.filter(paid=True).count())
