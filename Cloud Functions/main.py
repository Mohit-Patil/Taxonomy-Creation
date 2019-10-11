from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from flask import escape
import json
from collections import Counter

ml = discovery.build('ml', 'v1')
name = 'projects/{}/models/{}'.format('decent-oxygen-242311', 'stack_tag_predict')

def predict(request):
    request_json = request.get_json()
    print(request_json)
    question = ''

    if request_json and 'question' in request_json:
        question = request_json['question']

    label_arr = ['.htaccess', '.net', 'actionscript-3', 'ajax', 'algorithm',
       'android', 'android-layout', 'animation', 'apache', 'apache2',
       'api', 'arrays', 'asp.net', 'asp.net-mvc', 'asp.net-mvc-3',
       'audio', 'authentication', 'bash', 'c', 'c#', 'c#-4.0', 'c++',
       'caching', 'cakephp', 'calculus', 'class', 'cocoa', 'cocoa-touch',
       'codeigniter', 'command-line', 'core-data', 'css', 'css3',
       'database', 'database-design', 'date', 'datetime', 'debugging',
       'delphi', 'design', 'design-patterns', 'django', 'dns', 'dom',
       'drupal', 'eclipse', 'email', 'entity-framework', 'events',
       'excel', 'exception', 'facebook', 'facebook-graph-api', 'file',
       'firefox', 'flash', 'flex', 'forms', 'function', 'generics', 'git',
       'google', 'google-app-engine', 'google-chrome', 'google-maps',
       'grails', 'gui', 'gwt', 'haskell', 'hibernate', 'homework', 'html',
       'html5', 'http', 'iis', 'image', 'internet-explorer', 'ios',
       'ios5', 'ipad', 'iphone', 'java', 'java-ee', 'javascript',
       'jquery', 'jquery-ajax', 'jquery-mobile', 'jquery-ui', 'jsf',
       'json', 'jsp', 'linear-algebra', 'linq', 'linux', 'list',
       'listview', 'logging', 'loops', 'magento', 'math', 'matlab',
       'maven', 'memory', 'mod-rewrite', 'mongodb', 'ms-access',
       'multithreading', 'mvc', 'mysql', 'networking', 'nhibernate',
       'node.js', 'object', 'objective-c', 'oop', 'opengl',
       'optimization', 'oracle', 'osx', 'parsing', 'pdf', 'performance',
       'perl', 'permissions', 'phonegap', 'php', 'plugins', 'pointers',
       'postgresql', 'powershell', 'python', 'qt', 'query', 'r',
       'real-analysis', 'redirect', 'regex', 'rest', 'ruby',
       'ruby-on-rails', 'ruby-on-rails-3', 'scala', 'search', 'security',
       'servlets', 'session', 'sharepoint', 'shell', 'silverlight',
       'sockets', 'sorting', 'spring', 'sql', 'sql-server',
       'sql-server-2005', 'sql-server-2008', 'sqlite', 'ssh', 'ssl',
       'string', 'svn', 'swing', 'table', 'templates', 'testing',
       'tomcat', 'tsql', 'ubuntu', 'uitableview', 'unit-testing', 'unix',
       'url', 'validation', 'variables', 'vb.net', 'vba', 'video', 'vim',
       'visual-c++', 'visual-studio', 'visual-studio-2008',
       'visual-studio-2010', 'wcf', 'web-applications', 'web-services',
       'winapi', 'windows', 'windows-7', 'windows-8', 'windows-phone-7',
       'windows-server-2008', 'windows-xp', 'winforms', 'wordpress',
       'wpf', 'xaml', 'xcode', 'xml', 'xslt', 'zend-framework']

    response = ml.projects().predict(
        name=name,
        body={'instances': [question]}
    ).execute()

    return_str = ''
    tags = {}
   

    if 'error' in response:
        return_str = response['error']
        raise RuntimeError(response['error'])
    else:
        probabilities = response['predictions'][0]
        for i,val in enumerate(probabilities):
            print(i,val)
            if val > 0.1:
            	tags[label_arr[i]] = val
        from collections import Counter 
        k = Counter(tags) 
        TAG = []
  
        # Finding 4 highest values 
        high = k.most_common(4)  
        for i in high: 
             TAG.append(i[0])
        
        return_str = ','.join(TAG)
        if len(return_str) == 0:
            return_str = 'No tags found.'
    
    print(return_str)
    return json.dumps({'resp': return_str})