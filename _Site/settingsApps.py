print('Loads Chat Settings ... ', end='')
# Chat settings
CHAT_WS_SERVER_HOST = 'localhost'
CHAT_WS_SERVER_PORT = 5002
CHAT_WS_SERVER_PROTOCOL = 'ws'
CHAT_SERVER_STARTUP = True
print(' DONE')

if CHAT_SERVER_STARTUP:
    print('startUp Chat ')



print('Loads HelpDesk Settings ... ', end='')


# django-helpdesk configuration settings
# You can override django-helpdesk's defaults by redefining them here.
# To see what settings are available, see the docs/configuration.rst
# file for more information.
# Some common settings are below.

HELPDESK_DEFAULT_SETTINGS = {
            'use_email_as_submitter': True,
            'email_on_ticket_assign': True,
            'email_on_ticket_change': True,
            'login_view_ticketlist': True,
            'email_on_ticket_apichange': True,
            'preset_replies': True,
            'tickets_per_page': 25
}

# Should the public web portal be enabled?
HELPDESK_PUBLIC_ENABLED = True
HELPDESK_VIEW_A_TICKET_PUBLIC = True
HELPDESK_SUBMIT_A_TICKET_PUBLIC = True

# Should the Knowledgebase be enabled?
HELPDESK_KB_ENABLED = True

# Allow users to change their passwords
HELPDESK_SHOW_CHANGE_PASSWORD = True

# Instead of showing the public web portal first,
# we can instead redirect users straight to the login page.
HELPDESK_REDIRECT_TO_LOGIN_BY_DEFAULT = False
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'
print(' DONE')


# apiSettings
APIDebug = True
