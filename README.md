graphite
========
Graphite on Django via Nodejs via Drupal

## Installation
This codebase runs off of python virtualenv.

<pre>
# Get the source
git clone git@github.com:khalib/cs-education.git graphite

# Create the virtual environment
virtualenv ./graphite/
cd graphite

# Source the activate settings.
source bin/activate

# Install the libraries.
pip install -r requirements.txt
</pre>

Add this code to the top of the activate settings file in **bin/activate**:
<pre>
DJANGO_SETTINGS_MODULE="graphite.settings_local"
export DJANGO_SETTINGS_MODULE
</pre>

Re-source the activate settings:
<pre>
source bin/activate
</pre>

Run the server:
<pre>
python manage.py runserver
</pre>
