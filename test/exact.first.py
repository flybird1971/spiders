__author__ = 'flybird1971'

# use test python some script

import urllib2

index = 0
for line in urllib2.urlopen('http://www.pythondoc.com/pythontutorial27/stdlib.html'):
   line = line.decode('utf-8')  # Decoding the binary data to text.
   if 'EST' in line or 'EDT' in line:  # look for Eastern Time
       print("+"*45)
       index += 1
       print(index)
       print line

print('end....')

# email
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('1607450455@qq.com', '1607450455@qq.com',"""To: jcaesar@example.org
    From: soothsayer@example.org
    Beware the Ides of March.
    """)
server.quit()

# date
# dates are easily constructed and formatted
from datetime import date
now = date.today()
datetime.date(2003, 12, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days