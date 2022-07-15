# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from calcasa.api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from calcasa.api.model.aanvraagdoel import Aanvraagdoel
from calcasa.api.model.adres import Adres
from calcasa.api.model.adres_info import AdresInfo
from calcasa.api.model.adres_info_adres import AdresInfoAdres
from calcasa.api.model.adres_info_notities import AdresInfoNotities
from calcasa.api.model.bestemmingsdata import Bestemmingsdata
from calcasa.api.model.bodem_status_type import BodemStatusType
from calcasa.api.model.bodemdata import Bodemdata
from calcasa.api.model.business_rules_code import BusinessRulesCode
from calcasa.api.model.business_rules_problem_details import BusinessRulesProblemDetails
from calcasa.api.model.callback import Callback
from calcasa.api.model.cbs_indeling import CbsIndeling
from calcasa.api.model.energielabel import Energielabel
from calcasa.api.model.factuur import Factuur
from calcasa.api.model.foto import Foto
from calcasa.api.model.fundering_data_bron import FunderingDataBron
from calcasa.api.model.fundering_herstel_type import FunderingHerstelType
from calcasa.api.model.fundering_risico import FunderingRisico
from calcasa.api.model.fundering_risico_label import FunderingRisicoLabel
from calcasa.api.model.fundering_soort_bron import FunderingSoortBron
from calcasa.api.model.fundering_type import FunderingType
from calcasa.api.model.fundering_typering import FunderingTypering
from calcasa.api.model.funderingdata import Funderingdata
from calcasa.api.model.funderingdata_bio_infectie_risico import FunderingdataBioInfectieRisico
from calcasa.api.model.funderingdata_droogstand_risico import FunderingdataDroogstandRisico
from calcasa.api.model.funderingdata_optrekkend_vocht_risico import FunderingdataOptrekkendVochtRisico
from calcasa.api.model.funderingdata_typering import FunderingdataTypering
from calcasa.api.model.gebiedsdata import Gebiedsdata
from calcasa.api.model.geldverstrekker import Geldverstrekker
from calcasa.api.model.http_validation_problem_details import HttpValidationProblemDetails
from calcasa.api.model.invalid_argument_problem_details import InvalidArgumentProblemDetails
from calcasa.api.model.json_patch_document import JsonPatchDocument
from calcasa.api.model.klantwaarde_type import KlantwaardeType
from calcasa.api.model.kwartaal import Kwartaal
from calcasa.api.model.modeldata import Modeldata
from calcasa.api.model.not_found_problem_details import NotFoundProblemDetails
from calcasa.api.model.notitie import Notitie
from calcasa.api.model.notities import Notities
from calcasa.api.model.objectdata import Objectdata
from calcasa.api.model.omgevingsdata import Omgevingsdata
from calcasa.api.model.omgevingsdata_buurt import OmgevingsdataBuurt
from calcasa.api.model.omgevingsdata_gemeente import OmgevingsdataGemeente
from calcasa.api.model.omgevingsdata_land import OmgevingsdataLand
from calcasa.api.model.omgevingsdata_provincie import OmgevingsdataProvincie
from calcasa.api.model.omgevingsdata_wijk import OmgevingsdataWijk
from calcasa.api.model.operation import Operation
from calcasa.api.model.operation_type import OperationType
from calcasa.api.model.permissions_denied_problem_details import PermissionsDeniedProblemDetails
from calcasa.api.model.problem_details import ProblemDetails
from calcasa.api.model.product_type import ProductType
from calcasa.api.model.rapport import Rapport
from calcasa.api.model.referentieobject import Referentieobject
from calcasa.api.model.referentieobject_adres import ReferentieobjectAdres
from calcasa.api.model.referentieobject_cbs_indeling import ReferentieobjectCbsIndeling
from calcasa.api.model.referentieobject_object import ReferentieobjectObject
from calcasa.api.model.resource_exhausted_problem_details import ResourceExhaustedProblemDetails
from calcasa.api.model.taxatiedata import Taxatiedata
from calcasa.api.model.taxatiestatus import Taxatiestatus
from calcasa.api.model.validation_problem_details import ValidationProblemDetails
from calcasa.api.model.verkoop_bijzonderheden import VerkoopBijzonderheden
from calcasa.api.model.vorige_verkoop import VorigeVerkoop
from calcasa.api.model.waardering import Waardering
from calcasa.api.model.waardering_cbs_indeling import WaarderingCbsIndeling
from calcasa.api.model.waardering_factuur import WaarderingFactuur
from calcasa.api.model.waardering_input_parameters import WaarderingInputParameters
from calcasa.api.model.waardering_model import WaarderingModel
from calcasa.api.model.waardering_object import WaarderingObject
from calcasa.api.model.waardering_ontwikkeling import WaarderingOntwikkeling
from calcasa.api.model.waardering_ontwikkeling_kwartaal import WaarderingOntwikkelingKwartaal
from calcasa.api.model.waardering_ontwikkeling_kwartaal_kwartaal import WaarderingOntwikkelingKwartaalKwartaal
from calcasa.api.model.waardering_originele_input import WaarderingOrigineleInput
from calcasa.api.model.waardering_rapport import WaarderingRapport
from calcasa.api.model.waardering_status import WaarderingStatus
from calcasa.api.model.waardering_taxatie import WaarderingTaxatie
from calcasa.api.model.waardering_webhook_payload import WaarderingWebhookPayload
from calcasa.api.model.waardering_zoek_parameters import WaarderingZoekParameters
from calcasa.api.model.woning_type import WoningType
