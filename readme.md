# prop-updater

prop-updater adds/edits [Inforegister ID](https://www.wikidata.org/wiki/Property:P9321)
on wikidata items where [Business Registry code](https://www.wikidata.org/wiki/Property:P6518) is present.

Inforegister ID props are generated using .xlsx, which is made up of 2 cols: 
Business Registry code, beautified Inforegister URL.

`pip install -r config/req.txt`

Example execution:

`python3 prop-updater.py 'urlid.xlsx' 'BotUserName' 'BotPassword'`
