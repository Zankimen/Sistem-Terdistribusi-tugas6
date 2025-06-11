from flask import Flask, request, Response, jsonify

app = Flask(__name__)

def generate_content(size, content_type):
    if content_type == 'html':
        content = '<!DOCTYPE html>\n<html>\n<head>\n<title>Response File</title>\n</head>\n<body>\n'
        content += '<h1>Ini adalah file HTML response</h1>\n'
        footer = '</body>\n</html>'
        target_size = size - len(content.encode('utf-8')) - len(footer.encode('utf-8'))
        paragraph = '<p>'
        lorem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        while len((content + paragraph + footer).encode('utf-8')) < size:
            paragraph += lorem_text
        paragraph += '</p>\n'
        content += paragraph + footer
    else:
        content = 'Ini adalah file TXT response\n\n'
        lorem_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
        while len(content.encode('utf-8')) < size:
            content += lorem_text

    actual_size = len(content.encode('utf-8'))
    if actual_size > size:
        content = content[:-(actual_size - size)]

    return content

def calculate_size(size_param):
    size_param = str(size_param).lower()
    sizes = {
        'small': 10 * 1024,
        'medium': 100 * 1024,
        'large': 500 * 1024,
        'xlarge': 1024 * 1024,
        'xxlarge': int(1.5 * 1024 * 1024)
    }

    if size_param in sizes:
        return sizes[size_param]
    try:
        return int(size_param) * 1024
    except ValueError:
        return 10 * 1024

@app.route('/', methods=['POST'])
def generate_file():
    """
    Endpoint POST untuk menerima JSON body:
    {
        "size": "medium",
        "type": "html"
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid JSON'}), 400

    size_param = data.get('size', 'small')
    content_type = data.get('type', 'txt').lower()

    size_bytes = calculate_size(size_param)
    content = generate_content(size_bytes, content_type)
    mimetype = 'text/html' if content_type == 'html' else 'text/plain'

    return Response(content, mimetype=mimetype)

@app.route('/', methods=['GET'])
def index():
    return '''
    
    <p>Contoh JSON body:</p>
    <pre>{
  "size": "medium",
  "type": "html"
}</pre>
    <p>Ukuran bisa: small, medium, large, xlarge, xxlarge, atau angka dalam KB</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
