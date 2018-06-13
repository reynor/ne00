python /opt/ne00/acme_tiny.py --account-key /opt/ne00/account.key --csr /opt/ne00/domain.csr --acme-dir /opt/ne00/challenges/ > /opt/ne00/signed.crt || exit
wget -O - https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem > /opt/ne00/intermediate.pem
cat /opt/ne00/signed.crt /opt/ne00/intermediate.pem > /opt/ne00/chained.pem
nginx -s reload