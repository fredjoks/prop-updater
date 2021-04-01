import pandas as pd
import sys

from logger import logger

from wikidata import get_companies, get_qids, deploy_one

log = logger(__name__)

source_xlsx = {
    'path': str(sys.argv[1]),
    'cols': ['reg_code', 'url']
}


def main():
    log.info('quering company map...')
    company_map = get_companies()

    log.info('quering Qid map...')
    qid_map = get_qids()
    print(type(qid_map))

    log.info('reading xlsx into dataframe...')
    try:
        df = pd.read_excel(source_xlsx['path'], names=source_xlsx['cols'])
    except IOError as e:
        log.exception(e)
        return

    log.info('checking Inforegister ID props...')
    for qid, reg_code in company_map.items():
        url = df[df['reg_code'] == int(reg_code)].url
        if not len(url):
            log.warning(f'url not found for reg_code {reg_code}')
            continue

        ir_prop = url.item().split('/')[-1]
        if ir_prop in qid_map:
            log.info(f'{qid} up-to-date')
            continue

        try:
            deploy_one(qid, ir_prop)
        except Exception as e:
            log.error(f'wikidata_id {qid} reg_code {reg_code}')
            log.exception(e)


if __name__ == "__main__":
    main()
