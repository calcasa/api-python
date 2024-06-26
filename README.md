# calcasa-api
The Calcasa API is used to connect to Calcasa provided services. This is the first production version of the service

## Client packages
[Nuget](https://www.nuget.org/packages/Calcasa.Api) - [Packagist](https://packagist.org/packages/calcasa/api) - [PyPI](https://pypi.org/project/calcasa.api)
## Client implementation notes
Clients should at all times be tolerant to the following:

- Extra fields in responses
- Empty or hidden fields in responses
- Extra values in enumerations
- Unexpected error responses in the form of [Problem Details](https://rfc-editor.org/rfc/rfc7807)

## OpenAPI Specification
This API is documented in **OpenAPI format version 3** you can use tools like the [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) to generate API clients for for example the languages we don't provide a pre-built client for. This is documented [here](/api/v1/articles/clients/generation).

## Changelog

### 2024-05-14 (v1.3.1)
- Add `DeelWaarderingWebhookPayload` model.
- Use of strings for CBS codes. 
    - Add `buurtCode` field to `CbsIndeling` model.
    - Allow for string input for endpoint `buurt`.
- Add UserAgent header to callback requests with format: CalcasaPublicAPI/`<version>`

### 2023-11-14 (v1.3.0)
- Add `geldverstrekker` field to the `CallbackInschrijving` model.
- Add support for mTLS on the callback service.
    - By default when requested by the target server the public CA signed TLS certificate with the appropriate domain as Common Name will be offered as the client certificate. 
    - Public TLS Certificates rotate every couple of months.
- Change a couple of `date-time` fields that only contained a date to pure `date` fields. This might result is a different type in the generated clients and the service-side validation will be more strict. Times included in values will no longer be silently dropped, but will generate an error.
    - Change `Modeldata` model `waardebepalingsdatum` field to type `date` in OpenAPI spec.
    - Change `Bestemmingsdata` model `datumBestemmingplan` field to type `date` in OpenAPI spec.
    - Change `Bodemdata` model `datumLaatsteOnderzoek` field to type `date` in OpenAPI spec.
    - Change `Referentieobject` model `verkoopdatum` field to type `date` in OpenAPI spec.
    - Change `VorigeVerkoop` model `verkoopdatum` field to type `date` in OpenAPI spec.
    - Change `waarderingInputParameters` model `peildatum` field to type `date` in OpenAPI spec. This is an input field and will now require a date without a time.
- Add `desktopTaxatieHerwaardering` product to enumeration `ProductType`.
- The service no longer returns CORS headers.
- Actions now correctly report the 'application/problem+json' Content-Type in the documentation for the `HTTP 422 Unprocessable Entity` responses.
- Added `energielabelData` field to `Objectdata` model to contain the extra information about the energy label.
- The OpenAPI spec generation was changed slightly and thus the generated and published clients might be affected. There might be some slight breaking changes at compile time, but the functionality remains the same.
    - For example for C# and PHP `AdresInfoAdres` is now just covered by `Adres`
    - Likewise for the `Omgevingsdata*` models that are now all covered by `Gebiedsdata`
    - For a lot of the `Waardering*` models they are now using the correct model names, like `WaarderingModel` -> `Modeldata`


### 2023-04-17 (v1.2.1)
- Add `externeReferentie` field to the `CallbackInschrijving` and `WaarderingWebhookPayload` models.

### 2022-08-04 (v1.2.0)
- Add support for managing `CallbackSubscription`'s, this allows you to subscribe to callbacks for valuations that were not created with your API client.
    - `GET /v1/callbacks/inschrijvingen`
    - `POST /v1/callbacks/inschrijvingen`
    - `GET /v1/callbacks/inschrijvingen/{bagNummeraanduidingId}`
    - `DELETE /v1/callbacks/inschrijvingen/{bagNummeraanduidingId}`
- Add `taxateurnaam` field to the `Taxatiedata` model.
- Callback URIs should now end in `/` not just contain it to help stop common errors (ending in `=` is also still allowed when using a query string).
- Updating configuration in the `POST /v1/configuratie/callbacks` endpoint now clears stored but decommissioned versions from the configuration object.
- Add `klantkenmerk` to the `WaarderingInputParameters` and `Waardering` models.

### 2022-07-12 (v1.1.7)
- Added support for the OAuth 2.0 authorization code flow for use of the API with user accounts.
- Add `bouweenheid` to `FunderingSoortBron` enumeration.

### 2022-05-19 (v1.1.6)
- Added `ltvTeHoogOverbrugging` value to the `BusinessRulesCode` enumeration.

### 2022-04-13 (v1.1.5)
- Fix the schema for `Operation` `value` field for the benefit of the PHP and Python code generators, these will now correctly support any value type.

### 2022-04-12 (v1.1.4)
- Added proper Content-Disposition headers to the `GET /v1/rapporten/{id}` and `GET /v1/facturen/{id}` endpoints with the correct filename.
- Fix Mime Types for the `POST /v1/configuratie/callbacks` endpoint to only accept `application/json`.
- Fix C# API client to correctly use the `application/json-patch+json` content type in requests that require it.
- Fix C# client's `FileParameter` type correct handling of response headers like `Content-Disposition` and `Content-Type`.
- Removed C# client's useless implementation of `IValidatableObject`.
- Fix Python client's internal namespace name being illegal `calcasa-api` -> `calcasa.api`.

### 2022-03-22 (v1.1.3)
- Add 402 (Payment required) and 422 (Unprocessable entity) as potential response for `PATCH /v1/waarderingen/{id}`.

### 2022-03-17 (v1.1.2)
- Fixed response type for `GET /v1/geldverstrekkers/{productType}` endpoint.

### 2022-03-08 (v1.1.1)
- Added `GET /v1/geldverstrekkers/{productType}` endpoint.
- Restored all `ProblemDetails` models.

### 2022-03-07 (v1.1.0)
- Added `isErfpacht` to `WaarderingInputParameters`.
- Cleaned up serialization of null values, they should no longer appear in the output.

### 2021-02-04
- Added extra clarification to the documentation pertaining to the `WaarderingInputParameters` and which fields are required for the different input parameter combinations.

### 2022-01-11 (v1.0.2)
- Fixed `GET /api/v1/bodem/{id}` endpoint path parameter description, query parameter was never meant to be there.

### 2021-12-23
- Clarified the documentation pertaining to the `WaarderingInputParameters` and which fields are required for the different product types.

### 2021-12-22 (v1.0.1)
- Dates are now serialized in the ISO date-only format `yyyy-MM-dd` to stop any confusion around timezones and are all assumed to be in UTC.
    - `peildatum` in `WaarderingsInputParameters`
    - `datum_bestemmingplan` in `Bestemmingsdata`
    - `datum_laatste_onderzoek` in `Bodemdata`
    - `verkoopdatum` in `Referentieobject`
    - `verkoopdatum` in `VorigeVerkoop`
    - `waardebepalingsdatum` in `Modeldata`
- Reintroduced the `WaarderingWebhookPayload` model that was omitted.

### 2021-12-21
- Patching the status of a `Waardering` object will now immediatly reflect its new status in the response object.

### 2021-12-13 (v1.0.0)
- Initial release of `v1` based on `v0.0.6`

## Cross-Origin Resource Sharing
This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with [W3C spec](https://www.w3.org/TR/cors/).
And that allows cross-domain communication from the browser.
All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.

## Authentication
Authentication is done via [OAuth2](https://oauth.net/2/) and the [client credentials](https://oauth.net/2/grant-types/client-credentials/) grant type.

## Previous versions changelogs

### 2022-02-02
- API version `v0` was removed from service.

### 2021-12-23
- Mark `v0` as officially deprecated. No further versions will be released. Every implementation should move to `v1`

### 2021-12-10 (v0.0.6)
- Added extra field `peildatum` to the `WaarderingInputParameters` model.

### 2021-11-25 (v0.0.5)
- Updated all reported OAuth2 scopes and reduced the superflous scope information on each endpoint.

### 2021-11-23 (v0.0.4)
- Added per square meter developments to the `WaarderingOntwikkeling` object (fields with the `PerVierkantemeter` suffix).

### 2021-11-15 (v0.0.3)
- Added callback update and read endpoints and models.
- Updated documentation.

### 2021-11-11
- Renamed /fundering endpoint to /funderingen to be more in line with other endpoints
- Renamed `HerstelType` to `FunderingHerstelType`.
- Added `FunderingType` values.

### 2021-11-10
- Adjusted OpenAPI Spec generation to fix some issues with certain generators. This also means that the nullable nature of certain fields is now correctly represented. Please refer to the Generation article for more information, the config files were updated aswell.

### 2021-11-09
- Added `Status` and `Taxatiedatum` to `Taxatiedata` model.

### 2021-11-08
- Renamed `id` field in `AdresInfo` model to `bagNummeraanduidingId`.
- Added `GET /v0/fundering/{id}` endpoint with corresponding models.
- Changed HTTP response code for the `BusinessRulesProblemDetails` error return type of `POST /v0/waardering` from `422 Unprocessable Entity` to `406 Not Acceptable` to fix a duplicate.

### 2021-10-13
- Added `taxatie` field to `Waardering` model.
- Added `Taxatiedata` model containing the `taxatieorganisatie` field for desktop valuations.

### 2021-09-29
- Added `aangemaakt` timestamp field to `Waardering` model.
- Added `WaarderingZoekParameters` model to replace `WaarderingInputParameters` in the `POST /v0/waarderingen/zoeken` endpoint.
- Split `Omgevingsdata` model into a set of separate `Gebiedsdata` models that also contain extra statistics.
- Added `bijzonderheden` field to `VorigeVerkoop` model.
- Renamed `ReferentieBijzonderheden` model to `VerkoopBijzonderheden`.

### 2021-09-22
- Initial release of `v0`

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.3.1
- Package version: 1.3.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.calcasa.nl/contact](https://www.calcasa.nl/contact)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import calcasa.api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import calcasa.api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import calcasa.api
from pprint import pprint
from calcasa.api.api import adressen_api
from calcasa.api.model.adres import Adres
from calcasa.api.model.adres_info import AdresInfo
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
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

# Configure OAuth2 access token for authorization: oauth
configuration = calcasa.api.Configuration(
    host = "https://api.calcasa.nl"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with calcasa.api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = adressen_api.AdressenApi(api_client)
    bag_nummeraanduiding_id = 1 # int | Een BAG Nummeraanduiding ID om een adres te specificeren.

    try:
        # Adres info op basis van BAG Nummeraanduiding Id.
        api_response = api_instance.get_adres(bag_nummeraanduiding_id)
        pprint(api_response)
    except calcasa.api.ApiException as e:
        print("Exception when calling AdressenApi->get_adres: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.calcasa.nl*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdressenApi* | [**get_adres**](docs/AdressenApi.md#get_adres) | **GET** /api/v1/adressen/{bagNummeraanduidingId} | Adres info op basis van BAG Nummeraanduiding Id.
*AdressenApi* | [**search_adres**](docs/AdressenApi.md#search_adres) | **POST** /api/v1/adressen/zoeken | Zoek adres info op basis van het gegeven adres.
*BestemmingsplannenApi* | [**get_bestemming_by_id**](docs/BestemmingsplannenApi.md#get_bestemming_by_id) | **GET** /api/v1/bestemmingsplannen/{bagNummeraanduidingId} | Gegevens over de bestemmingsplannen op de locatie van een adres (BAG Nummeraanduiding ID).
*BodemApi* | [**get_bodem_by_id**](docs/BodemApi.md#get_bodem_by_id) | **GET** /api/v1/bodem/{bagNummeraanduidingId} | Gegevens over de bodemkwaliteit op de locatie van een adres (BAG Nummeraanduiding ID).
*BuurtApi* | [**get_buurt**](docs/BuurtApi.md#get_buurt) | **GET** /api/v1/buurt/{buurtCode} | Gegevens over een buurt en de wijk, gemeente en land waarin deze buurt gesitueerd is.
*CallbacksApi* | [**add_or_update_callback_subscription**](docs/CallbacksApi.md#add_or_update_callback_subscription) | **POST** /api/v1/callbacks/inschrijvingen | Voeg een callback inschrijving toe (of werk bij) voor de huidige client voor een adres.
*CallbacksApi* | [**delete_notification_subscription**](docs/CallbacksApi.md#delete_notification_subscription) | **DELETE** /api/v1/callbacks/inschrijvingen/{bagNummeraanduidingId} | Verwijder de callback inschrijving voor deze client, dit adres en optioneel een geldverstrekker.
*CallbacksApi* | [**get_notification_subscription**](docs/CallbacksApi.md#get_notification_subscription) | **GET** /api/v1/callbacks/inschrijvingen/{bagNummeraanduidingId} | Haal de callback inschrijving op voor deze client, dit adres en eventueel opgegeven geldverstrekker.
*CallbacksApi* | [**get_notification_subscriptions**](docs/CallbacksApi.md#get_notification_subscriptions) | **GET** /api/v1/callbacks/inschrijvingen | Haal de callback inschrijvingen binnen voor deze client.
*ConfiguratieApi* | [**get_callbacks**](docs/ConfiguratieApi.md#get_callbacks) | **GET** /api/v1/configuratie/callbacks | Haal de geconfigureerde callback URL&#39;s op voor de huidige client.
*ConfiguratieApi* | [**update_callbacks**](docs/ConfiguratieApi.md#update_callbacks) | **POST** /api/v1/configuratie/callbacks | Configureer callback URL voor een specifieke API versie voor de huidige client.
*FacturenApi* | [**get_factuur**](docs/FacturenApi.md#get_factuur) | **GET** /api/v1/facturen/{id} | Factuur op basis van een waardering Id.
*FotosApi* | [**get_foto**](docs/FotosApi.md#get_foto) | **GET** /api/v1/fotos/{id} | Foto op basis van een foto Id.
*FunderingenApi* | [**get_fundering_by_id**](docs/FunderingenApi.md#get_fundering_by_id) | **GET** /api/v1/funderingen/{bagNummeraanduidingId} | Gegevens over de fundering op de locatie van een adres (BAG Nummeraanduiding ID).
*GeldverstrekkersApi* | [**get_geldverstrekkers**](docs/GeldverstrekkersApi.md#get_geldverstrekkers) | **GET** /api/v1/geldverstrekkers/{productType} | Alle geldverstrekkers die te gebruiken zijn voor aanvragen.
*RapportenApi* | [**get_rapport**](docs/RapportenApi.md#get_rapport) | **GET** /api/v1/rapporten/{id} | Rapport op basis van waardering Id.
*WaarderingenApi* | [**create_waardering**](docs/WaarderingenApi.md#create_waardering) | **POST** /api/v1/waarderingen | Creërt een waardering.
*WaarderingenApi* | [**get_waardering**](docs/WaarderingenApi.md#get_waardering) | **GET** /api/v1/waarderingen/{id} | Waardering op basis van Id.
*WaarderingenApi* | [**get_waardering_ontwikkeling**](docs/WaarderingenApi.md#get_waardering_ontwikkeling) | **GET** /api/v1/waarderingen/{id}/ontwikkeling | Waardering ontwikkeling op basis van waardering Id.
*WaarderingenApi* | [**patch_waarderingen**](docs/WaarderingenApi.md#patch_waarderingen) | **PATCH** /api/v1/waarderingen/{id} | Patcht een waardering.
*WaarderingenApi* | [**search_waarderingen**](docs/WaarderingenApi.md#search_waarderingen) | **POST** /api/v1/waarderingen/zoeken | Zoek waardering op basis van input parameters.


## Documentation For Models

 - [Aanvraagdoel](docs/Aanvraagdoel.md)
 - [Adres](docs/Adres.md)
 - [AdresInfo](docs/AdresInfo.md)
 - [Bestemmingsdata](docs/Bestemmingsdata.md)
 - [BodemStatusType](docs/BodemStatusType.md)
 - [Bodemdata](docs/Bodemdata.md)
 - [BusinessRulesCode](docs/BusinessRulesCode.md)
 - [BusinessRulesProblemDetails](docs/BusinessRulesProblemDetails.md)
 - [Callback](docs/Callback.md)
 - [CallbackInschrijving](docs/CallbackInschrijving.md)
 - [CbsIndeling](docs/CbsIndeling.md)
 - [DeelWaarderingWebhookPayload](docs/DeelWaarderingWebhookPayload.md)
 - [Energielabel](docs/Energielabel.md)
 - [EnergielabelData](docs/EnergielabelData.md)
 - [Factuur](docs/Factuur.md)
 - [Foto](docs/Foto.md)
 - [FunderingDataBron](docs/FunderingDataBron.md)
 - [FunderingHerstelType](docs/FunderingHerstelType.md)
 - [FunderingRisico](docs/FunderingRisico.md)
 - [FunderingRisicoLabel](docs/FunderingRisicoLabel.md)
 - [FunderingSoortBron](docs/FunderingSoortBron.md)
 - [FunderingType](docs/FunderingType.md)
 - [FunderingTypering](docs/FunderingTypering.md)
 - [Funderingdata](docs/Funderingdata.md)
 - [Gebiedsdata](docs/Gebiedsdata.md)
 - [Geldverstrekker](docs/Geldverstrekker.md)
 - [InvalidArgumentProblemDetails](docs/InvalidArgumentProblemDetails.md)
 - [JsonPatchDocument](docs/JsonPatchDocument.md)
 - [KlantwaardeType](docs/KlantwaardeType.md)
 - [Kwartaal](docs/Kwartaal.md)
 - [Modeldata](docs/Modeldata.md)
 - [NotFoundProblemDetails](docs/NotFoundProblemDetails.md)
 - [Notitie](docs/Notitie.md)
 - [Notities](docs/Notities.md)
 - [Objectdata](docs/Objectdata.md)
 - [Omgevingsdata](docs/Omgevingsdata.md)
 - [Operation](docs/Operation.md)
 - [OperationType](docs/OperationType.md)
 - [PermissionsDeniedProblemDetails](docs/PermissionsDeniedProblemDetails.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ProductType](docs/ProductType.md)
 - [Rapport](docs/Rapport.md)
 - [Referentieobject](docs/Referentieobject.md)
 - [ResourceExhaustedProblemDetails](docs/ResourceExhaustedProblemDetails.md)
 - [Taxatiedata](docs/Taxatiedata.md)
 - [Taxatiestatus](docs/Taxatiestatus.md)
 - [ValidationProblemDetails](docs/ValidationProblemDetails.md)
 - [VerkoopBijzonderheden](docs/VerkoopBijzonderheden.md)
 - [VorigeVerkoop](docs/VorigeVerkoop.md)
 - [Waardering](docs/Waardering.md)
 - [WaarderingInputParameters](docs/WaarderingInputParameters.md)
 - [WaarderingOntwikkeling](docs/WaarderingOntwikkeling.md)
 - [WaarderingOntwikkelingKwartaal](docs/WaarderingOntwikkelingKwartaal.md)
 - [WaarderingStatus](docs/WaarderingStatus.md)
 - [WaarderingWebhookPayload](docs/WaarderingWebhookPayload.md)
 - [WaarderingZoekParameters](docs/WaarderingZoekParameters.md)
 - [WoningType](docs/WoningType.md)


## Documentation For Authorization


## oauth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **all**: Full permissions for all areas.
 - **api:all**: Full permissions for all areas of the public API.
 - **api:bestemmingsplannen:all**: Full permissions for the bestemmingsplannen area of the public API.
 - **api:bodem:all**: Full permissions for the bodem area of the public API.
 - **api:buurt:all**: Full permissions for the buurt area of the public API.
 - **api:configuratie:all**: Full permissions for the configuratie area of the public API.
 - **api:callback:all**: Full permissions for the callback area of the public API.
 - **api:facturen:all**: Full permissions for the facturen area of the public API.
 - **api:fotos:all**: Full permissions for the fotos area of the public API.
 - **api:funderingen:all**: Full permissions for the funderingen area of the public API.
 - **api:rapporten:all**: Full permissions for the rapporten area of the public API.
 - **api:waarderingen:all**: Full permissions for the waarderingen area of the public API.
 - **api:adressen:read**: Read permissions for the adressen area of the public API.
 - **api:bestemmingsplannen:read**: Read permissions for the bestemmingsplannen area of the public API.
 - **api:bodem:read**: Read permissions for the bodem area of the public API.
 - **api:buurt:read**: Read permissions for the buurt area of the public API.
 - **api:configuratie:read**: Read permissions for the configuratie area of the public API.
 - **api:configuratie:write**: Write permissions for the configuratie area of the public API.
 - **api:callback:read**: Read permissions for the callback area of the public API.
 - **api:callback:write**: Write permissions for the callback area of the public API.
 - **api:facturen:read**: Read permissions for the facturen area of the public API.
 - **api:fotos:read**: Read permissions for the fotos area of the public API.
 - **api:funderingen:read**: Read permissions for the funderingen area of the public API.
 - **api:geldverstrekkers:read**: Read permissions for the geldverstrekkers area of the public API.
 - **api:rapporten:read**: Read permissions for the rapporten area of the public API.
 - **api:waarderingen:create**: Create permissions for the waarderingen area of the public API.
 - **api:waarderingen:patch**: Patch permissions for the waarderingen area of the public API.
 - **api:waarderingen:read**: Read permissions for the waarderingen area of the public API.
 - **api:waarderingen:ontwikkeling**: Read permissions for the ontwikkelingen endpoint in the waarderingen area of the public API.


## oauth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://authentication.01.staging.calcasa.nl/oauth2/v2.0/authorize
- **Scopes**: 
 - **all**: Full permissions for all areas.
 - **api:all**: Full permissions for all areas of the public API.
 - **api:bestemmingsplannen:all**: Full permissions for the bestemmingsplannen area of the public API.
 - **api:bodem:all**: Full permissions for the bodem area of the public API.
 - **api:buurt:all**: Full permissions for the buurt area of the public API.
 - **api:configuratie:all**: Full permissions for the configuratie area of the public API.
 - **api:callback:all**: Full permissions for the callback area of the public API.
 - **api:facturen:all**: Full permissions for the facturen area of the public API.
 - **api:fotos:all**: Full permissions for the fotos area of the public API.
 - **api:funderingen:all**: Full permissions for the funderingen area of the public API.
 - **api:rapporten:all**: Full permissions for the rapporten area of the public API.
 - **api:waarderingen:all**: Full permissions for the waarderingen area of the public API.
 - **api:adressen:read**: Read permissions for the adressen area of the public API.
 - **api:bestemmingsplannen:read**: Read permissions for the bestemmingsplannen area of the public API.
 - **api:bodem:read**: Read permissions for the bodem area of the public API.
 - **api:buurt:read**: Read permissions for the buurt area of the public API.
 - **api:configuratie:read**: Read permissions for the configuratie area of the public API.
 - **api:configuratie:write**: Write permissions for the configuratie area of the public API.
 - **api:callback:read**: Read permissions for the callback area of the public API.
 - **api:callback:write**: Write permissions for the callback area of the public API.
 - **api:facturen:read**: Read permissions for the facturen area of the public API.
 - **api:fotos:read**: Read permissions for the fotos area of the public API.
 - **api:funderingen:read**: Read permissions for the funderingen area of the public API.
 - **api:geldverstrekkers:read**: Read permissions for the geldverstrekkers area of the public API.
 - **api:rapporten:read**: Read permissions for the rapporten area of the public API.
 - **api:waarderingen:create**: Create permissions for the waarderingen area of the public API.
 - **api:waarderingen:patch**: Patch permissions for the waarderingen area of the public API.
 - **api:waarderingen:read**: Read permissions for the waarderingen area of the public API.
 - **api:waarderingen:ontwikkeling**: Read permissions for the ontwikkelingen endpoint in the waarderingen area of the public API.


## Author

info@calcasa.nl


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in calcasa.api.apis and calcasa.api.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from calcasa.api.api.default_api import DefaultApi`
- `from calcasa.api.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import calcasa.api
from calcasa.api.apis import *
from calcasa.api.models import *
```

