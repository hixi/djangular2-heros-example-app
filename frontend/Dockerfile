FROM  nginx:alpine
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# Copy built app to wwwroot
COPY dist /usr/share/nginx/html
