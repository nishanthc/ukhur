
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# Ukhur [![CodeFactor](https://www.codefactor.io/repository/github/nishanthc/ukhur/badge)](https://www.codefactor.io/repository/github/snishanthc/ukhur)


Ukhur is a Django application that allows you to analyse multiple .txt files. The analyis consisnts of identifying the
 number of occurrences of words in one or many .txt files. The application allows you to identify which sentences
 each unique word appears in.
 
 Once a report is generated it is persistant, it can be shared with other people to view.
 
# Demo Site [![Website ukhur.nish.io](https://img.shields.io/website-up-down-green-red/http/ukhur.nish.io.svg)](http://ukhur.nish.io/)


A hosted instance of Ukhur can be accessed by clicking [here](http://ukhur.nish.io). You can find sample files to upload here.
 Remember to try and upload multiple files at the same time.
 
 If you'd like to see a pre-generated report on a EULA from Microsoft you can view it [here](https://ukhur.nish.io/report/f199d881-5a5e-47be-9c47-ba84f54766ad/).
 
 
## Getting Started

There are three ways this application has been designed to be operate.

* Vanilla Local - (Development)
    * This requires you to follow the prerequisites and configuration guide.
    
* Docker - (Local + Production) 
    * This does not require any prerequisites/configuration apart from Docker being installed on your system.

* AWS Elasticbeanstalk - (Production)
    * You only need to create an Amazon RDS postgres Database and store the associated variables in your EB environments enviornment variables. 
    The .ebextensions will configure the rest of environment for you.
     However you are required to have knowledge of configuring the apache_ssl.config to suit your domain name.


### Prerequisites

If you would like to run this application without docker you are required to have an operational Postgres database.

#### Python Packages

It is recommended a python virtual environment is created for this application and then the following
command is executed to install all required python packages:

```
pip install -r requirements.txt
```

#### Installing NLTK Data (local only)

For any local installations it is required that NLTK data is downloaded manually. This can be doing by running executing the following commands within your python environment:

```
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

### Configuration

This application uses environment variables to keep variables outside of the code base in order to improve security.
At this moment the only environment variables which are required are related to the database.

If you'd like to run this application locally you need a` local.env`, if you'd like to run this in
 production you require a `production.env`:

The .env files must exist in `ukhur/settings`.
 
```
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_user_password
DATABASE_HOST=your_db_host
DATABASE_PORT=your_db_port
```

### Database Migrations

If you are attempting to run this application locally you will have to manually migrate the database by using the following command:

```
python manage.py migrate --settings=ukhur.settings.local
```

### Running Ukhur Locally

In order to run Ukhur locally you can use the following command:
```
python manage.py runserver --settings=ukhur.settings.local
```

## Built With

* [NLTK](http://www.dropwizard.io/1.0.2/docs/) - Natural Language Toolkit

## Authors

* **Nishanth Chandradas** - - [Linkedin](https://www.linkedin.com/in/nishanthchandradas/)


## License 

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


