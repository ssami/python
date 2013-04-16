"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime 
from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse

from polls.models import Poll

def create_poll(question, days) : 
	return Poll.objects.create(question=question, pub_date=timezone.now() + datetime.timedelta(days=days))

class PollMethodTests (TestCase) : 
	
	def test_was_published_recently_with_future_poll (self) : 
		"""
		was_published_recently() should return False for polls whose 
		pub_date is in the future
		"""
		
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False) 
		
	def test_was_published_recently_with_recent_poll (self) : 
		"""
		was_published_recently() should return True for polls whose pub_date
		is within the last day
		"""
		
		recent_poll = Poll(pub_date=timezone.now() - datetime.timedelta(hours=1))
		self.assertEqual(recent_poll.was_published_recently(), True) 
		
	def test_was_published_recently_with_old_poll (self): 
		"""
		was_published_recently() should return False for polls whose pub_date
		is older than 1 day
		"""
		old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
		self.assertEqual(old_poll.was_published_recently(), False)


class PollViewTests (TestCase) : 
	def test_index_view_with_no_polls(self) : 
		"""
		If no polls exist, an appropriate message should be displayed
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No polls are available.')
		self.assertQuerysetEqual(response.context['latest_poll_list'], [])

	def test_index_view_with_a_past_poll(self) : 
		"""
		Polls with a pub_date in the past should be displayed on the index page
		"""
		create_poll(question="Past poll.", days=-30)
		response = self.client.get(reverse('polls:index')) 
		self.assertQuerysetEqual(
			response.context['latest_poll_list'],
			['<Poll: Past poll.>']
		)
		
	def test_index_view_with_a_future_poll (self) : 
		""" 
		Polls with a pub_date in the future should not be displayed
		"""
		create_poll(question="Future poll", days=30); 
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, "No polls are available.", status_code=200)
		self.assertQuerysetEqual(response.context['latest_poll_list'], [])
		
	
##INCLUDE TEST PAST + PRESENT POLL, TWO PAST POLLS
### https://docs.djangoproject.com/en/1.5/intro/tutorial05/
