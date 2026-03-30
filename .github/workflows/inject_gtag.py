import os

gtag_id = os.environ.get('GTAG_ID', '')
if not gtag_id:
    print("No GTAG_ID secret set, skipping.")
    exit(0)

snippet = (
    '<!-- Google tag (gtag.js) -->\n'
    '    <script async src="https://www.googletagmanager.com/gtag/js?id=' + gtag_id + '"></script>\n'
    '    <script>\n'
    '      window.dataLayer = window.dataLayer || [];\n'
    '      function gtag(){dataLayer.push(arguments);}\n'
    "      gtag('js', new Date());\n"
    "      gtag('config', '" + gtag_id + "');\n"
    '    </script>'
)

with open('index.html', 'r') as f:
    html = f.read()

html = html.replace('<!-- GTAG_PLACEHOLDER -->', snippet)

with open('index.html', 'w') as f:
    f.write(html)

print("Google Analytics tag injected.")
