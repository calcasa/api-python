"""
    Copyright 2022 Calcasa B.V.

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

    The version of the OpenAPI document: 1.1.7
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
from calcasa.api.model.funderingdata import Funderingdata
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails


class FunderingenApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_fundering_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (Funderingdata,),
                'auth': [
                    'oauth',
                    'oauth'
                ],
                'endpoint_path': '/api/v1/funderingen/{bagNummeraanduidingId}',
                'operation_id': 'get_fundering_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'bag_nummeraanduiding_id',
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
                },
                'attribute_map': {
                    'bag_nummeraanduiding_id': 'bagNummeraanduidingId',
                },
                'location_map': {
                    'bag_nummeraanduiding_id': 'path',
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

    def get_fundering_by_id(
        self,
        bag_nummeraanduiding_id,
        **kwargs
    ):
        """Gegevens over de fundering op de locatie van een adres (BAG Nummeraanduiding ID).  # noqa: E501

        Het funderingdata object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_fundering_by_id(bag_nummeraanduiding_id, async_req=True)
        >>> result = thread.get()

        Args:
            bag_nummeraanduiding_id (int): Een BAG Nummeraanduiding ID om een adres te specificeren.

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
            Funderingdata
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
        return self.get_fundering_by_id_endpoint.call_with_http_info(**kwargs)

