# calcasa.api.WaarderingenApi

All URIs are relative to *https://api.calcasa.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_waardering**](WaarderingenApi.md#create_waardering) | **POST** /api/v0/waarderingen | Creërt een waardering.
[**get_waardering**](WaarderingenApi.md#get_waardering) | **GET** /api/v0/waarderingen/{id} | Waardering op basis van Id.
[**get_waardering_ontwikkeling**](WaarderingenApi.md#get_waardering_ontwikkeling) | **GET** /api/v0/waarderingen/{id}/ontwikkeling | Waardering ontwikkeling op basis van Id.
[**patch_waarderingen**](WaarderingenApi.md#patch_waarderingen) | **PATCH** /api/v0/waarderingen/{id} | Patcht een waardering.
[**search_waarderingen**](WaarderingenApi.md#search_waarderingen) | **POST** /api/v0/waarderingen/zoeken | Zoek waardering op basis van input parameters.


# **create_waardering**
> Waardering create_waardering()

Creërt een waardering.

Nadat de waardering aangemaakt is zal deze bevestigd moeten worden. De velden die nodig zijn voor creatie het flow veld de parameters.  ### Callbacks | Name | Url | Schema | | --- | --- | --- | | waardering | {configuredWebhookUrl}/waardering | [WaarderingWebhookPayload](/api/v0/reference/schemas/WaarderingWebhookPayload) |  

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import waarderingen_api
from calcasa.api.model.validation_problem_details import ValidationProblemDetails
from calcasa.api.model.business_rules_problem_details import BusinessRulesProblemDetails
from calcasa.api.model.invalid_argument_problem_details import InvalidArgumentProblemDetails
from calcasa.api.model.waardering_input_parameters import WaarderingInputParameters
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.waardering import Waardering
from calcasa.api.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.calcasa.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waarderingen_api.WaarderingenApi(api_client)
    waardering_input_parameters = WaarderingInputParameters(
        geldverstrekker="geldverstrekker_example",
        product_type=None,
        hypotheekwaarde=1,
        aanvraagdoel=None,
        klantwaarde=1,
        klantwaarde_type=None,
        is_bestaande_woning=True,
        bag_nummeraanduiding_id=1,
        is_nhg=True,
        is_bestaande_nhg_hypotheek=True,
        benodigde_overbrugging=1,
    ) # WaarderingInputParameters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creërt een waardering.
        api_response = api_instance.create_waardering(waardering_input_parameters=waardering_input_parameters)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->create_waardering: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waardering_input_parameters** | [**WaarderingInputParameters**](WaarderingInputParameters.md)|  | [optional]

### Return type

[**Waardering**](Waardering.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | InvalidArgumentProblemDetails Invalid argument was provided.   Parameter productType is not a correct value.   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Permission denied while creating valuation.   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**406** | Business rules not passed.   |  -  |
**422** | Client Error |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waardering**
> Waardering get_waardering(id)

Waardering op basis van Id.

Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import waarderingen_api
from calcasa.api.model.validation_problem_details import ValidationProblemDetails
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.waardering import Waardering
from calcasa.api.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.calcasa.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waarderingen_api.WaarderingenApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Waardering op basis van Id.
        api_response = api_instance.get_waardering(id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->get_waardering: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Waardering**](Waardering.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | NotFoundProblemDetails Entity not found.   Could not find valuation.   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Permission denied while accessing valuation.   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**422** | Client Error |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waardering_ontwikkeling**
> WaarderingOntwikkeling get_waardering_ontwikkeling(id)

Waardering ontwikkeling op basis van Id.

Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import waarderingen_api
from calcasa.api.model.waardering_ontwikkeling import WaarderingOntwikkeling
from calcasa.api.model.validation_problem_details import ValidationProblemDetails
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.calcasa.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waarderingen_api.WaarderingenApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Waardering ontwikkeling op basis van Id.
        api_response = api_instance.get_waardering_ontwikkeling(id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->get_waardering_ontwikkeling: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**WaarderingOntwikkeling**](WaarderingOntwikkeling.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | NotFoundProblemDetails Entity not found.   Could not find valuation.   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Permission denied while accessing valuation.   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**422** | Client Error |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_waarderingen**
> Waardering patch_waarderingen(id)

Patcht een waardering.

Op dit moment kan alleen de waarderingsstatus gepatcht worden.  Dit endpoint kan gebruikt worden om een waarderingsinitialisatie te bevestingen.  ### Callbacks | Name | Url | Schema | | --- | --- | --- | | waardering | {configuredWebhookUrl}/waardering | [WaarderingWebhookPayload](/api/v0/reference/schemas/WaarderingWebhookPayload) |  

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import waarderingen_api
from calcasa.api.model.json_patch_document import JsonPatchDocument
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.invalid_argument_problem_details import InvalidArgumentProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.waardering import Waardering
from calcasa.api.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.calcasa.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waarderingen_api.WaarderingenApi(api_client)
    id = "id_example" # str | Het waarderings Id in de vorm van een UUID.
    json_patch_document = JsonPatchDocument([
        Operation(
            op=OperationType("add"),
            _from="/a/b/c",
            value={},
            path="/d/e/f",
        ),
    ]) # JsonPatchDocument | Het JsonPatch document voor de operatie. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patcht een waardering.
        api_response = api_instance.patch_waarderingen(id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->patch_waarderingen: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patcht een waardering.
        api_response = api_instance.patch_waarderingen(id, json_patch_document=json_patch_document)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->patch_waarderingen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Het waarderings Id in de vorm van een UUID. |
 **json_patch_document** | [**JsonPatchDocument**](JsonPatchDocument.md)| Het JsonPatch document voor de operatie. | [optional]

### Return type

[**Waardering**](Waardering.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | InvalidArgumentProblemDetails Invalid argument was provided.   Path /productType is readonly.   |  -  |
**404** | NotFoundProblemDetails Entity not found.   Could not find valuation.   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Permission denied while patching valuation.   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_waarderingen**
> [Waardering] search_waarderingen()

Zoek waardering op basis van input parameters.

Alle items kunnen gebruikt worden voor het zoeken,  ProductType en BagNummeraanduidingId zijn verplicht.  Het waardering object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import waarderingen_api
from calcasa.api.model.validation_problem_details import ValidationProblemDetails
from calcasa.api.model.waardering_zoek_parameters import WaarderingZoekParameters
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.waardering import Waardering
from calcasa.api.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to https://api.calcasa.nl
# See configuration.py for a list of all supported configuration parameters.
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waarderingen_api.WaarderingenApi(api_client)
    waardering_zoek_parameters = WaarderingZoekParameters(
        aangemaakt=dateutil_parser('1970-01-01T00:00:00.00Z'),
        geldverstrekker="geldverstrekker_example",
        product_type=None,
        aanvraagdoel=None,
        waardering_status=None,
        bag_nummeraanduiding_id=1,
    ) # WaarderingZoekParameters |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zoek waardering op basis van input parameters.
        api_response = api_instance.search_waarderingen(waardering_zoek_parameters=waardering_zoek_parameters)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling WaarderingenApi->search_waarderingen: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waardering_zoek_parameters** | [**WaarderingZoekParameters**](WaarderingZoekParameters.md)|  | [optional]

### Return type

[**[Waardering]**](Waardering.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Permission denied while accessing valuation.   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**422** | Client Error |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

