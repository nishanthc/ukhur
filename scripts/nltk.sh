source /opt/python/run/venv/bin/activate
export NLTK_DATA="/home/ec2-user/nltk_data/"
pip3 install nltk
python scripts/nltk_download.py
mv /home/ec2-user/nltk_data /usr/lib