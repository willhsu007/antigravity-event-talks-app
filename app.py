import os
import requests
import xml.etree.ElementTree as ET
from flask import Flask, jsonify, render_template

app = Flask(__name__)

FEED_URL = "https://docs.cloud.google.com/feeds/bigquery-release-notes.xml"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/release-notes')
def get_release_notes():
    try:
        response = requests.get(FEED_URL, timeout=10)
        response.raise_for_status()
        
        # 解析 XML
        root = ET.fromstring(response.content)
        
        # Atom feed standard namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        
        entries = []
        for entry in root.findall('atom:entry', ns):
            title_elem = entry.find('atom:title', ns)
            updated_elem = entry.find('atom:updated', ns)
            content_elem = entry.find('atom:content', ns)
            
            # 尋找 link (通常有 rel="alternate")
            link_elem = entry.find("atom:link[@rel='alternate']", ns)
            if link_elem is None:
                link_elem = entry.find("atom:link", ns)
            
            title = title_elem.text if title_elem is not None else "No Title"
            updated = updated_elem.text if updated_elem is not None else ""
            content = content_elem.text if content_elem is not None else ""
            link = link_elem.attrib.get('href', '') if link_elem is not None else ""
            
            entries.append({
                'title': title,
                'updated': updated,
                'content': content,
                'link': link
            })
            
        return jsonify({
            'status': 'success',
            'data': entries
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
