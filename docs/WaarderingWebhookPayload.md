# WaarderingWebhookPayload

De payload van de webhooks voor de waarderingen.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_name** | **str** |  | [optional] [readonly] 
**event_id** | **str** | Event Id | [optional] 
**waardering_id** | **str** | Waardering Id | [optional] 
**old_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The old status. | Waarde | Omschrijving | | --- | --- | | &#x60;onbekend&#x60; | Status onbekend. | | &#x60;initialiseren&#x60; | Deze waardering is geinitialiseerd maar moet nog bevestigd worden. | | &#x60;open&#x60; | Deze waardering is bevestigd maar moet nog uitgevoerd worden. | | &#x60;voltooid&#x60; | Deze waardering is voltooid. | | &#x60;opgewaardeerd&#x60; | Deze waardering is geupgrade naar een ander waardering type. | | &#x60;ongeldig&#x60; | Deze waardering is niet geldig, bijvoorbeeld omdat hij niet door de business rules is gekomen. | | &#x60;verlopen&#x60; | Deze waardering is verlopen omdat hij niet op tijd bevestigd is. | | &#x60;error&#x60; | Er is iets mis gegaan voor deze waardering. |    | [optional] 
**new_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The new status. | Waarde | Omschrijving | | --- | --- | | &#x60;onbekend&#x60; | Status onbekend. | | &#x60;initialiseren&#x60; | Deze waardering is geinitialiseerd maar moet nog bevestigd worden. | | &#x60;open&#x60; | Deze waardering is bevestigd maar moet nog uitgevoerd worden. | | &#x60;voltooid&#x60; | Deze waardering is voltooid. | | &#x60;opgewaardeerd&#x60; | Deze waardering is geupgrade naar een ander waardering type. | | &#x60;ongeldig&#x60; | Deze waardering is niet geldig, bijvoorbeeld omdat hij niet door de business rules is gekomen. | | &#x60;verlopen&#x60; | Deze waardering is verlopen omdat hij niet op tijd bevestigd is. | | &#x60;error&#x60; | Er is iets mis gegaan voor deze waardering. |    | [optional] 
**timestamp** | **datetime** | The event timestamp. | [optional] 
**is_test** | **bool** | Indicates whether this is a test valuation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


