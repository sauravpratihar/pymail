pymailer

Requirements

python >= 2.4



Edit the config file before running the script:

arguments: 
-s : normal mail
-t : test mail

./pymailer -s location_of_html_file.html location_of_csv_file.csv 'Email Subject'

eg: ./pymailer -s /home/file.html /home/file.csv 'test'



HTML File example:

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="en">
    <body>
        <h1>Test HTML Email - <!--name--></h1>
        <p>Hi <!--name-->, This is a test email from Pymailer - <a href="http://github.com:80/qoda/PyMailer/">http://github.com:80/qoda/PyMailer/</a>.</p>
    </body>
</html>


CSV File example:

name,email
Someones Name,someone@example.com
Someone Else,someone.else@example.com

OR you can create in excel too.