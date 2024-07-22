FROM ctftraining/base_image_nginx_mysql_php_73

COPY files /tmp/
RUN cp -rf /tmp/html /var/www/ \
    && cp -f /tmp/flag.sh /flag.sh \
    && cp -f /tmp/flag.txt /flag.txt \
    && chown -R www-data:www-data /var/www/html \
    && chmod 777 /flag.sh
