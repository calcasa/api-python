"""
    Copyright 2021 Calcasa B.V.

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

    The version of the OpenAPI document: 1.0.0
    Contact: info@calcasa.nl
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from calcasa-api.api_client import ApiClient, Endpoint as _Endpoint
from calcasa-api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from calcasa-api.model.business_rules_problem_details import BusinessRulesProblemDetails
from calcasa-api.model.invalid_argument_problem_details import InvalidArgumentProblemDetails
from calcasa-api.model.json_patch_document import JsonPatchDocument
from calcasa-api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa-api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa-api.model.problem_details import ProblemDetails
from calcasa-api.model.validation_problem_details import ValidationProblemDetails
from calcasa-api.model.waardering import Waardering
from calcasa-api.model.waardering_input_parameters import WaarderingInputParameters
from calcasa-api.model.waardering_ontwikkeling import WaarderingOntwikkeling
from calcasa-api.model.waardering_zoek_parameters import WaarderingZoekParameters


class WaarderingenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_waardering_endpoint = _Endpoint(
            settings={
                'response_type': (Waardering,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/api/v1/waarderingen',
                'operation_id': 'create_waardering',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'waardering_input_parameters',
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
                    'waardering_input_parameters':
                        (WaarderingInputParameters,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'waardering_input_parameters': 'body',
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
        self.get_waardering_endpoint = _Endpoint(
            settings={
                'response_type': (Waardering,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/api/v1/waarderingen/{id}',
                'operation_id': 'get_waardering',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
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
        self.get_waardering_ontwikkeling_endpoint = _Endpoint(
            settings={
                'response_type': (WaarderingOntwikkeling,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/api/v1/waarderingen/{id}/ontwikkeling',
                'operation_id': 'get_waardering_ontwikkeling',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
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
        self.patch_waarderingen_endpoint = _Endpoint(
            settings={
                'response_type': (Waardering,),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/api/v1/waarderingen/{id}',
                'operation_id': 'patch_waarderingen',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'json_patch_document',
                ],
                'required': [
                    'id',
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
                    'id':
                        (str,),
                    'json_patch_document':
                        (JsonPatchDocument,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                    'json_patch_document': 'body',
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
                    'application/json-patch+json'
                ]
            },
            api_client=api_client
        )
        self.search_waarderingen_endpoint = _Endpoint(
            settings={
                'response_type': ([Waardering],),
                'auth': [
                    'oauth'
                ],
                'endpoint_path': '/api/v1/waarderingen/zoeken',
                'operation_id': 'search_waarderingen',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'waardering_zoek_parameters',
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
                    'waardering_zoek_parameters':
                        (WaarderingZoekParameters,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'waardering_zoek_parameters': 'body',
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

    def create_waardering(
        self,
        **kwargs
    ):
        """Creërt een waardering.  # noqa: E501

        Nadat de waardering aangemaakt is zal deze bevestigd moeten worden. De BagNummeraanduidingId en ProductType velden zijn verplicht.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_waardering(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            waardering_input_parameters (WaarderingInputParameters): [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Waardering
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.create_waardering_endpoint.call_with_http_info(**kwargs)

    def get_waardering(
        self,
        id,
        **kwargs
    ):
        """Waardering op basis van Id.  # noqa: E501

        Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waardering(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): De waardering Id in de vorm van een UUID.

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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Waardering
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_waardering_endpoint.call_with_http_info(**kwargs)

    def get_waardering_ontwikkeling(
        self,
        id,
        **kwargs
    ):
        """Waardering ontwikkeling op basis van waardering Id.  # noqa: E501

        Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waardering_ontwikkeling(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): De waardering Id in de vorm van een UUID.

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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            WaarderingOntwikkeling
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.get_waardering_ontwikkeling_endpoint.call_with_http_info(**kwargs)

    def patch_waarderingen(
        self,
        id,
        **kwargs
    ):
        """Patcht een waardering.  # noqa: E501

        Op dit moment kan alleen de waarderingsstatus gepatcht worden.  Dit endpoint kan gebruikt worden om een waarderingsinitialisatie te bevestigen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_waarderingen(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): De waardering Id in de vorm van een UUID.

        Keyword Args:
            json_patch_document (JsonPatchDocument): Het JsonPatch document voor de operatie.. [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Waardering
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['id'] = \
            id
        return self.patch_waarderingen_endpoint.call_with_http_info(**kwargs)

    def search_waarderingen(
        self,
        **kwargs
    ):
        """Zoek waardering op basis van input parameters.  # noqa: E501

        Alle items kunnen gebruikt worden voor het zoeken, ProductType en BagNummeraanduidingId zijn verplicht.  Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_waarderingen(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            waardering_zoek_parameters (WaarderingZoekParameters): De parameters voor deze zoekopdracht.. [optional]
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
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Waardering]
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
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.search_waarderingen_endpoint.call_with_http_info(**kwargs)

