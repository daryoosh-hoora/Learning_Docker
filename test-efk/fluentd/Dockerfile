from	fluent/fluentd:v1.12.0-debian-1.0
user	root
run	gem uninstall -I elasticsearch && gem install elasticsearch -v 7.17.0
run	["gem","install","fluent-plugin-elasticsearch","--no-document","--version","5.0.3"]
user	fluent
