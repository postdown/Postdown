import json
import logging
from .ctor import MDDoc

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_rows(raw, keys):
    result = list()
    for i in raw:
        result.append([i.get(k, '') for k in keys])
    return result

# returns True if there are rows or a body in the request
def need_request_header(request):
    # get the query row count
    rows = []
    if 'query' in request['url']:
        rows = get_rows(
            request['url']['query'],
            ['key', 'value', 'description']
        )    

    need_header = len(rows) > 0 \
        or ('body' in request) \
        or ( ('header' in request) and request['header'] )

    logger.debug('need_request_header: %r', need_header)
    return need_header

def parse_api(doc, api):
    logger.info('Processing API: %s', api['name'])
    doc.title(api['name'], 2)
    request = api['request']
    url = request['url']['raw'] if isinstance(request['url'], dict) \
        else request['url']
    doc.code_block(
        '{0} {1}'.format(request['method'], url)
    )
    doc.block(request.get('description', ''))
    doc.hr()

    # Request information
    if need_request_header(request):
        doc.title('Request', 3)
        doc.comment_begin('Request information')
        
        if isinstance(request['url'], dict):
            rows = get_rows(
                request['url'].get('query',''),
                ['key', 'value', 'description']
            )

            if len(rows) > 0:
                # Request Query
                doc.bold('Query')
                doc.table(['Key', 'Value', 'Description'], rows)

        # Request Header
        if 'header' in request:
            doc.bold('Header')
            rows = get_rows(
                request['header'],
                ['key', 'value', 'description']
            )
            doc.table(['Key', 'Value', 'Description'], rows)

        # Request Body
        if 'body' in request:
            if 'mode' in request['body']:
                content = request['body'][request['body']['mode']]
                if request['body']['mode'] == 'file' and isinstance(content, dict):
                    content = content.get('src', '')

                if content:
                    doc.bold('Body')
                    if request['body']['mode'] in ['formdata', 'urlencoded']:
                        rows = get_rows(
                            request['body'][request['body']['mode']],
                            ['key', 'value', 'type', 'description']
                        )
                        doc.table(['Key', 'Value', 'Type', 'Description'], rows)
                    elif request['body']['mode'] == 'raw':
                        doc.code_block(request['body']['raw'])
                    elif request['body']['mode'] == 'file':
                        doc.text(request['body']['file']['src'])

        doc.comment_end('Request information')

    # Response example
    if len(api['response']) > 0:
        logger.info('Processing responses')
        doc.title('Examples:', 3)
        doc.comment_begin('Response example')
        for response in api['response']:
            logger.info('Processing Example: %s', response['name'])
            doc.bold('Example: {0}'.format(response['name']))
            doc.comment_begin('Example')

            # Original Request
            request = response['originalRequest']

            # Request URL
            url = request['url']['raw'] if isinstance(request['url'], dict) \
                else request['url']
            doc.code_block(
                '{0} {1}'.format(request['method'], url)
            )

            # Request Query
            if need_request_header(request):
                doc.bold('Request')
                doc.comment_begin('Request Query')

                if isinstance(request['url'], dict):
                    rows = []
                    if ('query' in request['url']):
                        rows = get_rows(
                            request['url']['query'],
                            ['key', 'value', 'description']
                        )

                    if len(rows) > 0:
                        doc.bold('Query')
                        doc.table(['Key', 'Value', 'Description'], rows)

                # Request Header
                if 'header' in request:
                    doc.bold('Header')
                    rows = get_rows(
                        request['header'],
                        ['key', 'value', 'description']
                    )
                    doc.table(['Key', 'Value', 'Description'], rows)

                # Request Body
                if 'body' in request:
                    if 'mode' in request['body']:
                        content = request['body'][request['body']['mode']]
                        if request['body']['mode'] == 'file' and \
                                isinstance(content, dict):
                            content = content.get('src', '')

                        if content:
                            doc.bold('Body')
                            if request['body']['mode'] in ['formdata', 'urlencoded']:
                                rows = get_rows(
                                    content,
                                    ['key', 'value', 'type', 'description']
                                )
                                doc.table(
                                    ['Key', 'Value', 'Type', 'Description'], rows
                                )
                            elif request['body']['mode'] == 'raw':
                                doc.code_block(request['body']['raw'])
                            elif request['body']['mode'] == 'file':
                                doc.text(request['body']['file']['src'])

                doc.comment_end('Request Query')
                doc.hr()

            if 'body' in response:
                doc.bold('Response')
                logger.info('Example Response')
                #logger.debug('response body: % s', response['body'])

                doc.comment_begin('Response')
                # doc.bold('Header')
                # header_rows = [[i['key'], i['value']] for i in response['header']]
                # doc.table(['Key', 'Value'], header_rows)
                doc.bold('Body')
                
                # don't assume the response is json
                try:
                    code_block = json.dumps(json.loads(response['body']), indent=2)
                except:
                    code_block = response['body']


                doc.code_block(code_block)
                doc.comment_end('Response')
            else:
                logger.warn('There was no response body, please make sure this is correct.')

            doc.comment_end('Example')
        doc.comment_end('Response example')
        doc.hr()


def parse(in_file, out_file):
    doc = MDDoc()

    with open(in_file) as f:
        collection = json.load(f)

    # The basic info.
    doc.title(collection['info']['name'])
    doc.hr()
    doc.line(collection['info'].get('description',''))
    doc.br()
    doc.hr()

    # API
    for folder in collection['item']:
        # check if there are sub folders
        if 'item' in folder:
            for api in folder['item']:
                parse_api(doc, api)
        else:
            # there are no sub-folders, so the "folder" is the api
            parse_api(doc, folder)

    with open(out_file, 'w+') as f:
        f.write(doc.output())
