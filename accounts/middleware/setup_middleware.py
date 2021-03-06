"""
Created on 26/07/2014

@author: antipro
"""
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class SetupMiddleware(object):

    IGNORE_PATHS = [
        reverse('accounts_setup'),
        reverse('set_user_password'),
        reverse('password_set_done'),
    ]

    def process_request(self, request):
        """If user did not config the account type yet then redirect them to do that
        """
        if request.user.is_authenticated():
            if not request.user.account_type and not request.path in self.IGNORE_PATHS:
                return redirect('accounts_setup')
