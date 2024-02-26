import pandas as pd
from sodapy import Socrata

def obtener_datos():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", departamento_nom='RISARALDA', limit=10)
    results_df = pd.DataFrame.from_records(results)
    return results_df