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

    Calcasa Public API v0

    The version of the OpenAPI document: 0.0.5
    Contact: info@calcasa.nl
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from calcasa-api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from calcasa-api.exceptions import ApiAttributeError



class WaarderingInputParameters(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'product_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'bag_nummeraanduiding_id': (int,),  # noqa: E501
            'geldverstrekker': (str,),  # noqa: E501
            'hypotheekwaarde': (int,),  # noqa: E501
            'aanvraagdoel': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'klantwaarde': (int,),  # noqa: E501
            'klantwaarde_type': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'is_bestaande_woning': (bool,),  # noqa: E501
            'is_nhg': (bool,),  # noqa: E501
            'is_bestaande_nhg_hypotheek': (bool,),  # noqa: E501
            'benodigde_overbrugging': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'product_type': 'productType',  # noqa: E501
        'bag_nummeraanduiding_id': 'bagNummeraanduidingId',  # noqa: E501
        'geldverstrekker': 'geldverstrekker',  # noqa: E501
        'hypotheekwaarde': 'hypotheekwaarde',  # noqa: E501
        'aanvraagdoel': 'aanvraagdoel',  # noqa: E501
        'klantwaarde': 'klantwaarde',  # noqa: E501
        'klantwaarde_type': 'klantwaardeType',  # noqa: E501
        'is_bestaande_woning': 'isBestaandeWoning',  # noqa: E501
        'is_nhg': 'isNhg',  # noqa: E501
        'is_bestaande_nhg_hypotheek': 'isBestaandeNhgHypotheek',  # noqa: E501
        'benodigde_overbrugging': 'benodigdeOverbrugging',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, product_type, bag_nummeraanduiding_id, *args, **kwargs):  # noqa: E501
        """WaarderingInputParameters - a model defined in OpenAPI

        Args:
            product_type (bool, date, datetime, dict, float, int, list, str, none_type):  | Waarde | Omschrijving | | --- | --- | | `onbekend` | Onbekend product type. Geen geldige invoer. | | `modelwaardeCalcasa` | Modelwaarde aanvraag met Calcasa Waardebepalingrapport. | | `modelwaardeRisico` | Modelwaarde aanvraag met risicorapport. | | `modelwaardeDesktopTaxatie` | Modelwaarde aanvraag met Desktop Taxatie Beknoptwaarderapport. | | `desktopTaxatie` | Desktop taxatie aanvraag met Desktop Taxatie rapport. |   
            bag_nummeraanduiding_id (int): Het BAG (Basisregistratie Adressen en Gebouwen) nummeraanduiding id.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            geldverstrekker (str): [optional]  # noqa: E501
            hypotheekwaarde (int): In hele euros.. [optional]  # noqa: E501
            aanvraagdoel (bool, date, datetime, dict, float, int, list, str, none_type): English: Request GoalEnglish: Request Goal | Waarde | Omschrijving | | --- | --- | | `onbekend` | English: Unknown | | `aankoopNieuweWoning` | English: New Home Purchase | | `overbruggingsfinanciering` | English: Bridge Financing | | `hypotheekOversluiten` | English: Refinancing Mortgage | | `hypotheekOphogen` | English: Increasing Mortage | | `hypotheekWijziging` | English: Changing Mortgage | | `hypotheekrenteWijzigen` | English: Change Mortgage Intrest |   . [optional]  # noqa: E501
            klantwaarde (int): In hele euros. De waarde zoals bekend bij de klant met bijbehorende KlantwaardeType.. [optional]  # noqa: E501
            klantwaarde_type (bool, date, datetime, dict, float, int, list, str, none_type):  | Waarde | Omschrijving | | --- | --- | | `onbekend` |  | | `koopsom` |  | | `taxatiewaarde` |  | | `wozWaarde` |  | | `eigenWaardeinschatting` |  |   . [optional]  # noqa: E501
            is_bestaande_woning (bool): Geeft aan of het te waarderen object een bestaande koopwoning is.. [optional]  # noqa: E501
            is_nhg (bool): Geeft aan of er gebruikt gemaakt wordt van de Nationale Hypotheekgarantie.. [optional]  # noqa: E501
            is_bestaande_nhg_hypotheek (bool): Geeft aan of er bij de eventuele bestaande hypotheek gebruik is gemaakt van de Nationale Hypotheekgarantie.. [optional]  # noqa: E501
            benodigde_overbrugging (int): In hele euros. Alleen van toepassing voor aanvraagdoel Overbruggingsfinanciering.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.product_type = product_type
        self.bag_nummeraanduiding_id = bag_nummeraanduiding_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, product_type, bag_nummeraanduiding_id, *args, **kwargs):  # noqa: E501
        """WaarderingInputParameters - a model defined in OpenAPI

        Args:
            product_type (bool, date, datetime, dict, float, int, list, str, none_type):  | Waarde | Omschrijving | | --- | --- | | `onbekend` | Onbekend product type. Geen geldige invoer. | | `modelwaardeCalcasa` | Modelwaarde aanvraag met Calcasa Waardebepalingrapport. | | `modelwaardeRisico` | Modelwaarde aanvraag met risicorapport. | | `modelwaardeDesktopTaxatie` | Modelwaarde aanvraag met Desktop Taxatie Beknoptwaarderapport. | | `desktopTaxatie` | Desktop taxatie aanvraag met Desktop Taxatie rapport. |   
            bag_nummeraanduiding_id (int): Het BAG (Basisregistratie Adressen en Gebouwen) nummeraanduiding id.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            geldverstrekker (str): [optional]  # noqa: E501
            hypotheekwaarde (int): In hele euros.. [optional]  # noqa: E501
            aanvraagdoel (bool, date, datetime, dict, float, int, list, str, none_type): English: Request GoalEnglish: Request Goal | Waarde | Omschrijving | | --- | --- | | `onbekend` | English: Unknown | | `aankoopNieuweWoning` | English: New Home Purchase | | `overbruggingsfinanciering` | English: Bridge Financing | | `hypotheekOversluiten` | English: Refinancing Mortgage | | `hypotheekOphogen` | English: Increasing Mortage | | `hypotheekWijziging` | English: Changing Mortgage | | `hypotheekrenteWijzigen` | English: Change Mortgage Intrest |   . [optional]  # noqa: E501
            klantwaarde (int): In hele euros. De waarde zoals bekend bij de klant met bijbehorende KlantwaardeType.. [optional]  # noqa: E501
            klantwaarde_type (bool, date, datetime, dict, float, int, list, str, none_type):  | Waarde | Omschrijving | | --- | --- | | `onbekend` |  | | `koopsom` |  | | `taxatiewaarde` |  | | `wozWaarde` |  | | `eigenWaardeinschatting` |  |   . [optional]  # noqa: E501
            is_bestaande_woning (bool): Geeft aan of het te waarderen object een bestaande koopwoning is.. [optional]  # noqa: E501
            is_nhg (bool): Geeft aan of er gebruikt gemaakt wordt van de Nationale Hypotheekgarantie.. [optional]  # noqa: E501
            is_bestaande_nhg_hypotheek (bool): Geeft aan of er bij de eventuele bestaande hypotheek gebruik is gemaakt van de Nationale Hypotheekgarantie.. [optional]  # noqa: E501
            benodigde_overbrugging (int): In hele euros. Alleen van toepassing voor aanvraagdoel Overbruggingsfinanciering.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.product_type = product_type
        self.bag_nummeraanduiding_id = bag_nummeraanduiding_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
