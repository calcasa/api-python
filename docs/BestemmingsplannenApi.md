# calcasa.api.BestemmingsplannenApi

All URIs are relative to *https://api.calcasa.nl*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bestemming_by_id**](BestemmingsplannenApi.md#get_bestemming_by_id) | **GET** /api/v0/bestemmingsplannen/{id} | Gegevens over de bestemmingsplannen op de locatie van een adres (BAG Nummeraanduiding ID).


# **get_bestemming_by_id**
> Bestemmingsdata get_bestemming_by_id(id)

Gegevens over de bestemmingsplannen op de locatie van een adres (BAG Nummeraanduiding ID).

Het bodemdata object zal gefilterd terug komen afhankelijk van het client_id wat gebruikt is voor de authenticatie.

### Example

* OAuth Authentication (oauth):

```python
import time
import calcasa.api
from calcasa.api.api import bestemmingsplannen_api
from calcasa.api.model.bestemmingsdata import Bestemmingsdata
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
    api_instance = bestemmingsplannen_api.BestemmingsplannenApi(api_client)
    id = 1 # int | Een BAG Nummeraanduiding ID om een adres te specificeren.

    # example passing only required values which don't have defaults set
    try:
        # Gegevens over de bestemmingsplannen op de locatie van een adres (BAG Nummeraanduiding ID).
        api_response = api_instance.get_bestemming_by_id(id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling BestemmingsplannenApi->get_bestemming_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Een BAG Nummeraanduiding ID om een adres te specificeren. |

### Return type

[**Bestemmingsdata**](Bestemmingsdata.md)

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

