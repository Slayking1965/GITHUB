# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class EndUserTypeList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the EndUserTypeList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeList
        """
        super(EndUserTypeList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/RegulatoryCompliance/EndUserTypes'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams EndUserTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EndUserTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypePage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return EndUserTypePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return EndUserTypePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a EndUserTypeContext

        :param sid: The unique string that identifies the End-User Type resource

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        """
        return EndUserTypeContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a EndUserTypeContext

        :param sid: The unique string that identifies the End-User Type resource

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        """
        return EndUserTypeContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.EndUserTypeList>'


class EndUserTypePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the EndUserTypePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypePage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypePage
        """
        super(EndUserTypePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EndUserTypeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        """
        return EndUserTypeInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.EndUserTypePage>'


class EndUserTypeContext(InstanceContext):
    """  """

    def __init__(self, version, sid):
        """
        Initialize the EndUserTypeContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the End-User Type resource

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        """
        super(EndUserTypeContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/RegulatoryCompliance/EndUserTypes/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the EndUserTypeInstance

        :returns: The fetched EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EndUserTypeInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.EndUserTypeContext {}>'.format(context)


class EndUserTypeInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, sid=None):
        """
        Initialize the EndUserTypeInstance

        :returns: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        """
        super(EndUserTypeInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'machine_name': payload.get('machine_name'),
            'fields': payload.get('fields'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: EndUserTypeContext for this EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeContext
        """
        if self._context is None:
            self._context = EndUserTypeContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the End-User Type resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def friendly_name(self):
        """
        :returns: A human-readable description of the End-User Type resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def machine_name(self):
        """
        :returns: A machine-readable description of the End-User Type resource
        :rtype: unicode
        """
        return self._properties['machine_name']

    @property
    def fields(self):
        """
        :returns: The required information for creating an End-User.
        :rtype: dict
        """
        return self._properties['fields']

    @property
    def url(self):
        """
        :returns: The absolute URL of the End-User Type resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the EndUserTypeInstance

        :returns: The fetched EndUserTypeInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.end_user_type.EndUserTypeInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.EndUserTypeInstance {}>'.format(context)
