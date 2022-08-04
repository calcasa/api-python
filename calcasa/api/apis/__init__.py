
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from calcasa.api.api.adressen_api import AdressenApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from calcasa.api.api.adressen_api import AdressenApi
from calcasa.api.api.bestemmingsplannen_api import BestemmingsplannenApi
from calcasa.api.api.bodem_api import BodemApi
from calcasa.api.api.buurt_api import BuurtApi
from calcasa.api.api.callbacks_api import CallbacksApi
from calcasa.api.api.configuratie_api import ConfiguratieApi
from calcasa.api.api.facturen_api import FacturenApi
from calcasa.api.api.fotos_api import FotosApi
from calcasa.api.api.funderingen_api import FunderingenApi
from calcasa.api.api.geldverstrekkers_api import GeldverstrekkersApi
from calcasa.api.api.rapporten_api import RapportenApi
from calcasa.api.api.waarderingen_api import WaarderingenApi
