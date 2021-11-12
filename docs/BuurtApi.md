# calcasa.api.BuurtApi

All URIs are relative to *https://api.calcasa.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buurt**](BuurtApi.md#get_buurt) | **GET** /api/v0/buurt/{id} | Gegevens over een buurt en de wijk, gemeente en land waarin deze buurt gesitueerd is.


# **get_buurt**
> Omgevingsdata get_buurt(id)

Gegevens over een buurt en de wijk, gemeente en land waarin deze buurt gesitueerd is.

Het omgevingdata object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import buurt_api
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
from calcasa.api.model.omgevingsdata import Omgevingsdata
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
    api_instance = buurt_api.BuurtApi(api_client)
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Gegevens over een buurt en de wijk, gemeente en land waarin deze buurt gesitueerd is.
        api_response = api_instance.get_buurt(id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling BuurtApi->get_buurt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  |

### Return type

[**Omgevingsdata**](Omgevingsdata.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | NotFoundProblemDetails Entity not found.   Kon buurt niet vinden   |  -  |
**403** | PermissionsDeniedProblemDetails Client does not have permission to perform this action.   Geen rechten   |  -  |
**401** | Provided credentials have expired.  Request was unauthenticated.   |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

