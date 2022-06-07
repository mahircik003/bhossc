#!/bin/bash
#!/usr/local/lib/python3.9
cd /root/bhossc
python3.9 manage.py runserver_plus --cert-file /etc/letsencrypt/live/bhos.svdev.me/cert.pem --key-file /etc/letsencrypt/live/bhos.svdev.me/privkey.pem bhos.svdev.me:8000
