<h2>pymailer</h2>

Requirements:
python >= 2.4



Edit the config file before running the script:

arguments: 
-s : normal mail
-t : test mail

./pymailer -s location_of_html_file.html location_of_csv_file.csv 'Email Subject'

eg: ./pymailer -s /home/file.html /home/file.csv 'test'



<h3>HTML File example:</h3>

```html
<html lang="en">
    <body>
        <h1>Test HTML Email</h1>
    </body>
</html>
```

<h3>CSV File example:</h3>

name,email
Someones Name,someone@example.com
Someone Else,someone.else@example.com

OR you can create in excel too.
