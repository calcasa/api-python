"""
    Copyright 2023 Calcasa B.V.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Calcasa Public API v1

    The version of the OpenAPI document: 1.3.1
    Contact: info@calcasa.nl
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from calcasa.api.api_client import ApiClient, Endpoint as _Endpoint
from calcasa.api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from calcasa.api.model.callback_inschrijving import CallbackInschrijving
from calcasa.api.model.invalid_argument_problem_details import InvalidArgumentProblemDetails
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails


class CallbacksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_or_update_callback_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (CallbackInschrijving,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/api/v1/callbacks/inschrijvingen',
                'operation_id': 'add_or_update_callback_subscription',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'callback_inschrijving',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'callback_inschrijving':
                        (CallbackInschrijving,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'callback_inschrijving': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_notification_subscription_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/api/v1/callbacks/inschrijvingen/{bagNummeraanduidingId}',
                'operation_id': 'delete_notification_subscription',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'bag_nummeraanduiding_id',
                    'geldverstrekker',
                ],
                'required': [
                    'bag_nummeraanduiding_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bag_nummeraanduiding_id':
                        (int,),
                    'geldverstrekker':
                        (str,),
                },
                'attribute_map': {
                    'bag_nummeraanduiding_id': 'bagNummeraanduidingId',
                    'geldverstrekker': 'geldverstrekker',
                },
                'location_map': {
                    'bag_nummeraanduiding_id': 'path',
                    'geldverstrekker': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_notification_subscription_endpoint = _Endpoint(
            settings={
                'response_type': (CallbackInschrijving,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/api/v1/callbacks/inschrijvingen/{bagNummeraanduidingId}',
                'operation_id': 'get_notification_subscription',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'bag_nummeraanduiding_id',
                    'geldverstrekker',
                ],
                'required': [
                    'bag_nummeraanduiding_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bag_nummeraanduiding_id':
                        (int,),
                    'geldverstrekker':
                        (str,),
                },
                'attribute_map': {
                    'bag_nummeraanduiding_id': 'bagNummeraanduidingId',
                    'geldverstrekker': 'geldverstrekker',
                },
                'location_map': {
                    'bag_nummeraanduiding_id': 'path',
                    'geldverstrekker': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_notification_subscriptions_endpoint = _Endpoint(
            settings={
                'response_type': ([CallbackInschrijving],),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/api/v1/callbacks/inschrijvingen',
                'operation_id': 'get_notification_subscriptions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def add_or_update_callback_subscription(
        self,
        **kwargs
    ):
        """Voeg een callback inschrijving toe (of werk bij) voor de huidige client voor een adres.  # noqa: E501

        De callback objecten zullen gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  Als er al een inschrijving bestaat voor dit adres dan wordt deze overschreven.  De inschrijvingen worden vanzelf opgeruimt als ze verlopen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_or_update_callback_subscription(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            callback_inschrijving (CallbackInschrijving): De te configureren callback inschrijving.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CallbackInschrijving
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.add_or_update_callback_subscription_endpoint.call_with_http_info(**kwargs)

    def delete_notification_subscription(
        self,
        bag_nummeraanduiding_id,
        **kwargs
    ):
        """Verwijder de callback inschrijving voor deze client, dit adres en optioneel een geldverstrekker.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_notification_subscription(bag_nummeraanduiding_id, async_req=True)
        >>> result = thread.get()

        Args:
            bag_nummeraanduiding_id (int):

        Keyword Args:
            geldverstrekker (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['bag_nummeraanduiding_id'] = \
            bag_nummeraanduiding_id
        return self.delete_notification_subscription_endpoint.call_with_http_info(**kwargs)

    def get_notification_subscription(
        self,
        bag_nummeraanduiding_id,
        **kwargs
    ):
        """Haal de callback inschrijving op voor deze client, dit adres en eventueel opgegeven geldverstrekker.  # noqa: E501

        Het callback object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notification_subscription(bag_nummeraanduiding_id, async_req=True)
        >>> result = thread.get()

        Args:
            bag_nummeraanduiding_id (int):

        Keyword Args:
            geldverstrekker (str): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CallbackInschrijving
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['bag_nummeraanduiding_id'] = \
            bag_nummeraanduiding_id
        return self.get_notification_subscription_endpoint.call_with_http_info(**kwargs)

    def get_notification_subscriptions(
        self,
        **kwargs
    ):
        """Haal de callback inschrijvingen binnen voor deze client.  # noqa: E501

        De callback objecten zullen gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notification_subscriptions(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [CallbackInschrijving]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.get_notification_subscriptions_endpoint.call_with_http_info(**kwargs)

