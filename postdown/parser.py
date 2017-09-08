import json
from .ctor import MDDoc


def parse(in_file, out_file):
    doc = MDDoc()

    with open(in_file) as f:
        collection = json.load(f)

    # The basic info.
    doc.title(collection['info']['name'])
    doc.hr()
    doc.line(collection['info']['description'])
    doc.br()
    doc.hr()

    # API
    for api in collection['item']:
        doc.title(api['name'], 2)
        request = api['request']
        doc.code_block('{0[method]} {0[url]}'.format(request))
        doc.block(request['description'])
        doc.hr()

        # Request information.
        doc.title('Request', 3)

        doc.comment_begin()
        doc.bold('Request Header')
        header_rows = [[i['key'], i['value'], i['description']] for i in request['header']]
        doc.table(['Key', 'Value', 'Description'], header_rows)
        doc.title('Request Body', 5)
        if request['body']['mode'] == 'raw':
            doc.code_block(request['body']['raw'])

        doc.comment_end()

        # Response example.
        doc.title('Examples:', 3)
        doc.comment_begin()
        for response in api['response']:
            doc.bold('Example: {0}'.format(response['name']))
            doc.comment_begin()
            doc.bold('Response Header')
            header_rows = [[i['key'], i['value']] for i in response['header']]
            doc.table(['Key', 'Value'], header_rows)
            doc.bold('Response Body')
            doc.code_block(json.dumps(json.loads(response['body']), indent=2))
            doc.comment_end()
        doc.comment_end()
        doc.hr()

    with open(out_file, 'w+') as f:
        f.write(doc.output())

