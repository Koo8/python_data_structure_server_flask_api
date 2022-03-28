import xml.etree.ElementTree as ET

data = '''
<person>
    <users>
        <user x="5">
            <name>Nancy</name>
            <id>001</id>
            <email y='hello'></email>
        </user>
        <user x="2">
            <name>grail</name>
            <id>002</id>
            <email y='bravo'></email>
        </user>
    </users>    
</person>'''

tree = ET.fromstring(data)
names = tree.findall('users/user/name')
for n in names:
    print(n.text)
