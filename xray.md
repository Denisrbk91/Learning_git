## ) Показать IP + порт клиента + процесс (чтобы видеть что это xray)

sudo ss -tnp state established 'sport = :443'