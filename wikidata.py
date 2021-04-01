import sys

from wikidataintegrator import wdi_core, wdi_login, wdi_helpers
from logger import logger

log = logger(__name__)

props = {
    'Inforegister ID': 'P9321',
    'Business Registry code': 'P6518'
}

login = wdi_login.WDLogin(user=str(sys.argv[2]), pwd=str(sys.argv[3]))


def deploy_one(qid, ir_prop, login=login, props=props):
    """Writes new data into wikidata element

    Args:
        qid (string): Q[1-9]\d*
        ir_prop (string): [0-9]{8}-[A-Z]+(-[A-Z]+)*
    """
    log.info(f'{qid} updating...')

    new_prop = wdi_core.WDString(
        value=ir_prop, prop_nr=props['Inforegister ID'])

    # data goes into a list, because many data objects can be provided
    data = [new_prop]

    wd_item = wdi_core.WDItemEngine(wd_item_id=qid, data=data)

    wd_item.write(login)


def get_qids(props=props):
    """Find wikidata elements where
    Inforegister ID prop is present.

    Returns:
        <class 'set'> {qid1, qid2, qid3}
    """
    qid_map = wdi_helpers.id_mapper(
        props['Inforegister ID'], return_as_set=True)

    return {k for k, _ in qid_map.items()}


def get_companies():
    """Find wikidata elements where
    Business Registry code is present

    Returns:
        <class 'dict'> {qid: reg_code}
    """
    company_map = wdi_helpers.id_mapper(
        props['Business Registry code'], return_as_set=True)

    return {list(v)[0]: k for k, v in company_map.items()}
