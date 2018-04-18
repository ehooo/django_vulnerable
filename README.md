# django_vulnerable
Is a vulnerable app for learn about web security

## Backend
  * Python 3
  * Django 2
  * Pipenv
  * Django Extensions

## Let Start
```
pipenv install
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Vulnerabilities

+ FTP Injection
+ Redis Injection
+ Mongo Injection
+ MQ Injection
+ LDAP Injection
+ [Django raw & extra](vulnerable/views/sql_injection.py)
+ [Python commands](vulnerable/views/commands.py)
+ [Python code](vulnerable/views/code.py)
+ [File inclusion](vulnerable/views/views.py)


## [Common Weakness Enumeration](http://cwe.mitre.org/index.html)

- [CWE-74](http://cwe.mitre.org/data/definitions/74.html):
  Injection

  _The software constructs all or part of a command, data structure,
  or record using externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify how it is parsed or
  interpreted when it is sent to a downstream component._

- [CWE-77](http://cwe.mitre.org/data/definitions/77.html):
  Improper Neutralization of Special Elements used in a Command ('Command Injection')

  _The software constructs all or part of a command using
  externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify the intended command
  when it is sent to a downstream component._

- [CWE-78](http://cwe.mitre.org/data/definitions/78.html):
  OS Command Injections

  _The software constructs all or part of an OS command using
  externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify the intended OS command
  when it is sent to a downstream component._

- [CWE-88](http://cwe.mitre.org/data/definitions/88.html):
  Argument Injection or Modification

  _The software does not sufficiently delimit the arguments
  being passed to a component in another control sphere,
  allowing alternate arguments to be provided,
  leading to potentially security-relevant changes_

- [CWE-89](http://cwe.mitre.org/data/definitions/91.html):
  Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')

  _The software constructs all or part of an SQL command using
  externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify the intended SQL command
  when it is sent to a downstream component._

- [CWE-90](http://cwe.mitre.org/data/definitions/90.html):
  Improper Neutralization of Special Elements used in an LDAP Query ('LDAP Injection')

  _The software constructs all or part of an LDAP query using
  externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify the intended LDAP query
  when it is sent to a downstream component._

- [CWE-91](http://cwe.mitre.org/data/definitions/91.html):
  XML Injection (aka Blind XPath Injection)

  _The software does not properly neutralize special elements
  that are used in XML, allowing attackers to modify the syntax,
  content, or commands of the XML before it is processed by an end system._

- [CWE-93](http://cwe.mitre.org/data/definitions/93.html):
  Improper Neutralization of CRLF Sequences ('CRLF Injection')

  _The software uses CRLF (carriage return line feeds)
  as a special element, e.g. to separate lines or records,
  but it does not neutralize or incorrectly neutralizes
  CRLF sequences from inputs._

- [CWE-94](http://cwe.mitre.org/data/definitions/94.html):
  Improper Control of Generation of Code ('Code Injection')

  _The software constructs all or part of a code segment using
  externally-influenced input from an upstream component,
  but it does not neutralize or incorrectly neutralizes
  special elements that could modify the syntax or
  behavior of the intended code segment._

- [CWE-99](http://cwe.mitre.org/data/definitions/99.html):
  Improper Control of Resource Identifiers ('Resource Injection')

  _	The software receives input from an upstream component,
  but it does not restrict or incorrectly restricts the input
  before it is used as an identifier for a resource that
  may be outside the intended sphere of control._
