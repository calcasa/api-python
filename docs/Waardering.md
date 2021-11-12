# Waardering


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id van de waardering of tracking Id. | [optional] 
**aangemaakt** | **datetime** | Het tijdsstempel van wanneer de waardering aangemaakt is. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | Waarde | Omschrijving | | --- | --- | | &#x60;onbekend&#x60; | Status onbekend. | | &#x60;initialiseren&#x60; | Deze waardering is geinitialiseerd maar moet nog bevestigd worden. | | &#x60;open&#x60; | Deze waardering is bevestigd maar moet nog uitgevoerd worden. | | &#x60;voltooid&#x60; | Deze waardering is voltooid. | | &#x60;opgewaardeerd&#x60; | Deze waardering is geupgrade naar een ander waardering type. | | &#x60;ongeldig&#x60; | Deze waardering is niet geldig, bijvoorbeeld omdat hij niet door de business rules is gekomen. | | &#x60;verlopen&#x60; | Deze waardering is verlopen omdat hij niet op tijd bevestigd is. | | &#x60;error&#x60; | Er is iets mis gegaan voor deze waardering. |    | [optional] 
**originele_input** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**adres** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**model** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**taxatie** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**object** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**cbs_indeling** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**fotos** | [**[Foto], none_type**](Foto.md) |  | [optional] 
**referenties** | [**[Referentieobject], none_type**](Referentieobject.md) |  | [optional] 
**vorige_verkopen** | [**[VorigeVerkoop], none_type**](VorigeVerkoop.md) |  | [optional] 
**rapport** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**factuur** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


