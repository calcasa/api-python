# calcasa.api.AdressenApi

All URIs are relative to *https://api.calcasa.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adres**](AdressenApi.md#get_adres) | **GET** /api/v0/adressen/{bagNummeraanduidingId} | Adres info op met het BAG Nummeraanduiding Id.
[**search_adres**](AdressenApi.md#search_adres) | **POST** /api/v0/adressen/zoeken | Zoek adres info op basis van het gegeven adres.


# **get_adres**
> AdresInfo get_adres(bag_nummeraanduiding_id)

Adres info op met het BAG Nummeraanduiding Id.

De Notities zullen leeg blijven voor dit endpoint.  Het adres object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import adressen_api
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
from calcasa.api.model.adres_info import AdresInfo
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
    api_instance = adressen_api.AdressenApi(api_client)
    bag_nummeraanduiding_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Adres info op met het BAG Nummeraanduiding Id.
        api_response = api_instance.get_adres(bag_nummeraanduiding_id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling AdressenApi->get_adres: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bag_nummeraanduiding_id** | **int**|  |

### Return type

[**AdresInfo**](AdresInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | NotFoundProblemDetails Entity not found.   Kon adres niet vinden   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Geen rechten   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_adres**
> AdresInfo search_adres()

Zoek adres info op basis van het gegeven adres.

De notities geven aan of de input al dan niet gewijzigd of onbekend is.  De enige velden die echt nodig zijn voor een compleet resultaat zijn de postcode, het huisnummer en de huisnummer toevoeging.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import adressen_api
from calcasa.api.model.adres import Adres
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
from calcasa.api.model.adres_info import AdresInfo
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
    api_instance = adressen_api.AdressenApi(api_client)
    adres = Adres(
        straat="Voorbeeldstraat",
        huisnummer=123,
        huisnummertoevoeging="A",
        postcode="1234AB",
        woonplaats="Voorbeeldstad",
    ) # Adres |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Zoek adres info op basis van het gegeven adres.
        api_response = api_instance.search_adres(adres=adres)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling AdressenApi->search_adres: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adres** | [**Adres**](Adres.md)|  | [optional]

### Return type

[**AdresInfo**](AdresInfo.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Geen rechten   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

